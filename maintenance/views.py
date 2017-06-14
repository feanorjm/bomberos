from django.shortcuts import render
from maintenance.forms import (BitacoraForm,
                               MantencionForm,
                               DetalleMantencionForm,
                               RepuestoDetalleMantencionForm,
                               MaquinaForm,
                               ConductorForm,
                               CombustibleForm,
                               CambioNeumaticoForm)

from maintenance.models import (Bitacora,
                                Mantencion,
                                DetalleMantencion,
                                RepuestoDetalleMantencion,
                                Maquina,
                                Conductor,
                                Carguios_combustible,
                                CambioNeumatico)

from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import JsonResponse, HttpResponse,HttpResponseRedirect

#VISTAS PARA BITACORA

@method_decorator(login_required, name='dispatch')
class BitacoraDetail(DetailView):
    #context_object_name = "bitacora_detail"
    model = Bitacora
    template_name = 'bitacora_detalle.html'


@method_decorator(login_required, name='dispatch')
class BitacoraList(ListView):
    model = Bitacora
    template_name = 'bitacora_list.html'


@method_decorator(login_required, name='dispatch')
class BitacoraCreateView(CreateView):
    form_class = BitacoraForm
    template_name = 'bitacora.html'
    #success_url = '/bitacora/add'

    def form_valid(self, form):
        kilometrajeform = form.cleaned_data['kilometraje_llegada']
        hodometroform = form.cleaned_data['hodometro_llegada']
        maquinaform = form.cleaned_data['maquina']
        maquina = Maquina.objects.get(nombre=maquinaform)
        maquina.kilometraje = kilometrajeform
        maquina.hodometro = hodometroform
        maquina.save()
        return super(BitacoraCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("bitacora_list")


@method_decorator(login_required, name='dispatch')
class BitacoraUpdateView(UpdateView):
    model = Bitacora
    form_class = BitacoraForm
    template_name = 'bitacora_update.html'


@method_decorator(login_required, name='dispatch')
class BitacoraDelete(DeleteView):
    model = Bitacora
    template_name = 'bitacora_delete.html'
    success_url = reverse_lazy('bitacora_list')

bitacora_detail = BitacoraDetail.as_view()
bitacora_list = BitacoraList.as_view()
bitacora_create_view = BitacoraCreateView.as_view()
bitacora_update = BitacoraUpdateView.as_view()
bitacora_delete = BitacoraDelete.as_view()

#VISTAS PARA MANTENCION

class AjaxableResponseMixin(object):
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def form_invalid(self, form):
        response = super(AjaxableResponseMixin, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super(AjaxableResponseMixin, self).form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
            }
            return JsonResponse(data)
        else:
            return response


class MantencionCreateView(AjaxableResponseMixin,CreateView):
    model = Mantencion
    form_class = MantencionForm
    template_name = 'mantencion_create.html'

    def get_success_url(self):
        return reverse("mantencion_create")

#mantencion_create = MantencionCreateView.as_view()

@login_required
def mantencion_create(request):
    mantencion_form = MantencionForm()
    detalle_mantencion_form = DetalleMantencionForm()
    if request.method == 'POST':
        mantencion_form = MantencionForm(request.POST)
        #book_formset = BookFormSet(request.POST, request.FILES, prefix='books')
        if mantencion_form.is_valid():
            mantencion_form.save()
            if request.is_ajax():
                data = {
                    'pk': Mantencion.objects.last().pk,
                }
                return JsonResponse(data)
        else:
            if request.is_ajax():
                return JsonResponse(mantencion_form.errors, status=400)
    else:
        return render(request, 'mantencion_create.html', {'form': mantencion_form,
                                                          'detalle_form':detalle_mantencion_form})

@login_required
def mantencion_add_detalle(request):
    if request.method == 'POST':
        detalle_mantencion_form = DetalleMantencionForm(request.POST)
        if detalle_mantencion_form.is_valid():
            detalle_mantencion_form.save()
            if request.is_ajax():
                data = {
                    'pk': DetalleMantencion.objects.last().pk,
                }
                return JsonResponse(data)
        else:
            if request.is_ajax():
                return JsonResponse(detalle_mantencion_form.errors, status=400)

@login_required
def mantencion_add_repuesto(request):
    if request.method == 'POST':
        repuesto_mantencion_form = RepuestoDetalleMantencionForm(request.POST)
        if repuesto_mantencion_form.is_valid():
            repuesto_mantencion_form.save()
            if request.is_ajax():
                data = {
                    'status': 'ok',
                }
                return JsonResponse(data)
        else:
            if request.is_ajax():
                return JsonResponse(repuesto_mantencion_form.errors, status=400)


@method_decorator(login_required, name='dispatch')
class MantencionListView(ListView):
    model = Mantencion
    template_name = 'mantencion_list.html'


@method_decorator(login_required, name='dispatch')
class MantencionDetailView(DetailView):
    model = Mantencion
    template_name = 'mantencion_detalle.html'

    #DEFINIR EL CONTEXT DATA Y HACER QUERYSET Y BUSCAR LOS DATOS DEL DETALLE Y LOS REPUESTOS

mantencion_list = MantencionListView.as_view()
mantencion_detail = MantencionDetailView.as_view()

#CRUD PARA MAQUINAS

@method_decorator(login_required, name='dispatch')
class MaquinaDetailView(DetailView):
    #context_object_name = "bitacora_detail"
    model = Maquina
    template_name = 'maquina_detail.html'


@method_decorator(login_required, name='dispatch')
class MaquinaListView(ListView):
    model = Maquina
    template_name = 'maquina_list.html'


@method_decorator(login_required, name='dispatch')
class MaquinaCreateView(CreateView):
    form_class = MaquinaForm
    template_name = 'maquina_create.html'

    def get_success_url(self):
        return reverse("maquina_list")


@method_decorator(login_required, name='dispatch')
class MaquinaUpdateView(UpdateView):
    model = Maquina
    form_class = MaquinaForm
    template_name = 'maquina_update.html'


@method_decorator(login_required, name='dispatch')
class MaquinaDeleteView(DeleteView):
    model = Maquina
    template_name = 'maquina_delete.html'
    success_url = reverse_lazy('maquina_list')

maquina_detail = MaquinaDetailView.as_view()
maquina_list = MaquinaListView.as_view()
maquina_create = MaquinaCreateView.as_view()
maquina_update = MaquinaUpdateView.as_view()
maquina_delete = MaquinaDeleteView.as_view()

#CRUD PARA CONDUCTORES

@method_decorator(login_required, name='dispatch')
class ConductorDetailView(DetailView):
    #context_object_name = "bitacora_detail"
    model = Conductor
    template_name = 'conductor_detail.html'

@method_decorator(login_required, name='dispatch')
class ConductorCreateView(CreateView):
    form_class = ConductorForm
    template_name = 'conductor_create.html'

    '''def form_valid(self, form):
        profile_image = Conductor(foto=self.get_form_kwargs().get('files')['foto'])
        profile_image.save()
        self.id = profile_image.id

        return HttpResponseRedirect(self.get_success_url())'''

    def get_success_url(self):
        return reverse("conductor_list")

@method_decorator(login_required, name='dispatch')
class ConductorListView(ListView):
    model = Conductor
    template_name = 'conductor_list.html'

@method_decorator(login_required, name='dispatch')
class ConductorUpdateView(UpdateView):
    model = Conductor
    form_class = ConductorForm
    template_name = 'conductor_update.html'

conductor_list = ConductorListView.as_view()
conductor_detail = ConductorDetailView.as_view()
conductor_create = ConductorCreateView.as_view()
conductor_update = ConductorUpdateView.as_view()

#CRUD PARA CARGA COMBUSTIBLE

@method_decorator(login_required, name='dispatch')
class CombustibleCreateView(CreateView):
    form_class = CombustibleForm
    template_name = 'combustible_create.html'

    def get_success_url(self):
        return reverse("combustible_list")

@method_decorator(login_required, name='dispatch')
class CombustibleListView(ListView):
    model = Carguios_combustible
    template_name = 'combustible_list.html'

combustible_create = CombustibleCreateView.as_view()
combustible_list = CombustibleListView.as_view()

#CRUD PARA CAMBIO NEUMATICOS

@method_decorator(login_required, name='dispatch')
class NeumaticosCreateView(CreateView):
    form_class = CambioNeumaticoForm
    template_name = 'neumaticos_create.html'

    def get_success_url(self):
        return reverse("neumaticos_list")

@method_decorator(login_required, name='dispatch')
class NeumaticosListView(ListView):
    model = CambioNeumatico
    template_name = 'neumaticos_list.html'

neumaticos_create = NeumaticosCreateView.as_view()
neumaticos_list = NeumaticosListView.as_view()