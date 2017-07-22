from django.shortcuts import render, get_object_or_404
from maintenance.forms import (BitacoraForm,
                               MantencionForm,
                               DetalleMantencionForm,
                               RepuestoDetalleMantencionForm,
                               MaquinaForm,
                               ConductorForm,
                               CombustibleForm
                               )

from maintenance.models import *

from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic import ListView, TemplateView
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
    #model = Bitacora
    template_name = 'bitacora_list.html'

    def get_queryset(self):
        if (self.request.user.username == 'admin'):
            queryset = Bitacora.objects.all().order_by('-fecha')
        else:
            user_comp = self.request.user.usuariocomp.compania.pk
            queryset = Bitacora.objects.filter(compania=user_comp).order_by('-fecha')

        return queryset


@method_decorator(login_required, name='dispatch')
class BitacoraCreateView(CreateView):
    form_class = BitacoraForm
    template_name = 'bitacora.html'
    #success_url = '/bitacora/add'

    def get_context_data(self, **kwargs):
        context = super(BitacoraCreateView, self).get_context_data(**kwargs)
        #context['username'] = self.request.user.username
        context['form'].fields['clave'].queryset = Clave.objects.exclude(nombre='6--14')

        if (self.request.user.username == 'admin'):
            context['form'].fields['compania'].queryset = Compania.objects.all()
        else:
            user_comp = self.request.user.usuariocomp.compania.pk
            context['form'].fields['compania'].queryset = Compania.objects.filter(pk=user_comp)
            print(context)
        return context


    def form_valid(self, form):
        kilometrajeform = form.cleaned_data['kilometraje_llegada']
        hodometroform = form.cleaned_data['hodometro_llegada']
        ho_bomba_regreso = form.cleaned_data['ho_bomba_regreso']
        maquinaform = form.cleaned_data['maquina']
        maquina = Maquina.objects.get(nombre=maquinaform)
        maquina.kilometraje = kilometrajeform
        maquina.hodometro = hodometroform
        maquina.hodometro_bomba = ho_bomba_regreso
        maquina.save()

        return super(BitacoraCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("bitacora_list")


@method_decorator(login_required, name='dispatch')
class BitacoraUpdateView(UpdateView):
    model = Bitacora
    form_class = BitacoraForm
    template_name = 'bitacora_update.html'

    def get_context_data(self, **kwargs):
        context = super(BitacoraUpdateView, self).get_context_data(**kwargs)
        #context['username'] = self.request.user.username
        context['form'].fields['clave'].queryset = Clave.objects.exclude(nombre='6--14')

        if (self.request.user.username == 'admin'):
            context['form'].fields['compania'].queryset = Compania.objects.all()
        else:
            user_comp = self.request.user.usuariocomp.compania.pk
            context['form'].fields['compania'].queryset = Compania.objects.filter(pk=user_comp)
            print(context)
        return context


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

#class MantencionCreateView(AjaxableResponseMixin,CreateView):
#class MantencionCreateView(CreateView):

@method_decorator(login_required, name='dispatch')
class MantencionCreateView(TemplateView):
    #model = Mantencion
    #form_class = MantencionForm
    #second_form_class = DetalleMantencionForm
    template_name = 'mantencion_create.html'

    #def get_success_url(self):
    #    return reverse("mantencion_create")

    def get(self, request, *args, **kwargs):
        form = MantencionForm(self.request.GET or None)
        form2 = DetalleMantencionForm(self.request.GET or None)
        context = self.get_context_data(**kwargs)
        context['form'] = form
        context['form2'] = form2
        if (self.request.user.username == 'admin'):
            context['form'].fields['compania'].queryset = Compania.objects.all()
        else:
            user_comp = self.request.user.usuariocomp.compania.pk
            context['form'].fields['compania'].queryset = Compania.objects.filter(pk=user_comp)
        return self.render_to_response(context)

@method_decorator(login_required, name='dispatch')
class MantencionFormView(FormView):
    form_class = MantencionForm
    template_name = 'mantencion_create.html'

    def form_valid(self, form):
        form.save()
        # guardar kilometraje y hodometro maquina
        kilometrajeform = form.cleaned_data['ki_regreso']
        hodometroform = form.cleaned_data['ho_regreso']
        maquinaform = form.cleaned_data['maquina']
        print(kilometrajeform, hodometroform, maquinaform)
        maquina = Maquina.objects.get(nombre=maquinaform)
        maquina.kilometraje = kilometrajeform
        maquina.hodometro = hodometroform
        maquina.save()
        # devolver pk a detalleForm
        if self.request.is_ajax():
            data = {
                'pk': Mantencion.objects.last().pk,
            }
            return JsonResponse(data)
        else:
            response = super(MantencionFormView, self).form_valid(form)
            return response

    def form_invalid(self, form):
        response = super(MantencionFormView, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

@method_decorator(login_required, name='dispatch')
class DetalleMantencionFormView(FormView):
    form_class = DetalleMantencionForm
    template_name = 'mantencion_create.html'

    def form_valid(self, form):
        form.save()
        if self.request.is_ajax():
            data = {
                'pk': DetalleMantencion.objects.last().pk,
            }
            return JsonResponse(data)
        else:
            response = super(DetalleMantencionFormView, self).form_valid(form)
            return response

    def form_invalid(self, form):
        response = super(DetalleMantencionFormView, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

@method_decorator(login_required, name='dispatch')
class RepuestoDetalleMantencionFormView(FormView):
    form_class = RepuestoDetalleMantencionForm
    template_name = 'mantencion_create.html'

    def form_valid(self, form):
        form.save()
        if self.request.is_ajax():
            data = {
                'status': 'ok',
                'pk': RepuestoDetalleMantencion.objects.last().pk,
            }
            return JsonResponse(data)
        else:
            response = super(RepuestoDetalleMantencionFormView, self).form_valid(form)
            return response

    def form_invalid(self, form):
        response = super(RepuestoDetalleMantencionFormView, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response



mantencion_create_view = MantencionCreateView.as_view() #GET
mantencion_form_view = MantencionFormView.as_view() #POST Mantencion
detalle_mantencion_form_view = DetalleMantencionFormView.as_view() #POST DetalleMantencion
repuesto_detalle_mantencion_form_view = RepuestoDetalleMantencionFormView.as_view() #POST RepuestoDetalleMantencion

@login_required
def get_parametros_maquina(request):
    if request.method == 'POST' and request.is_ajax():
        maquina = request.POST.get('maquina')
        print(maquina)
        parametros = Maquina.objects.filter(id=maquina).values('kilometraje','hodometro','tiene_bomba', 'hodometro_bomba')
        #conductores_maq = Conductor.objects.filter(maquina__nombre=maquina).values('id')
        print(parametros)
        return JsonResponse({'parametros': list(parametros)})


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

@login_required
def get_maquina_conductores(request):
    if request.method == 'POST' and request.is_ajax():
        compania = request.POST.get('compania')
        maquina = request.POST.get('maquina')
        #print(compania,maquina)
        conductores_com = Conductor.objects.filter(compania=compania).values('id','nombre','ap_paterno')
        conductores_maq = Conductor.objects.filter(maquina__nombre=maquina).values('id')
        #print(conductores_com)
        return JsonResponse({'conductores': list(conductores_com), 'cond_maq': list(conductores_maq)})


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

    def get_context_data(self, **kwargs):
        context = super(CombustibleCreateView, self).get_context_data(**kwargs)
        if (self.request.user.username == 'admin'):
            context['form'].fields['compania'].queryset = Compania.objects.all()
        else:
            user_comp = self.request.user.usuariocomp.compania.pk
            context['form'].fields['compania'].queryset = Compania.objects.filter(pk=user_comp)
            #print(context)
        return context

    def form_valid(self, form):
        #companiaform = form.cleaned_data['compania']
        #maquinaform = form.cleaned_data['maquina']
        litrosform = form.cleaned_data['litros']
        servicentroform  = form.cleaned_data['servicentro']
        km_salidaform  = form.cleaned_data['km_salida']
        hm_salidaform  = form.cleaned_data['hm_salida']
        km_regresoform  = form.cleaned_data['km_regreso']
        hm_regresoform  = form.cleaned_data['hm_regreso']
        valorform  = form.cleaned_data['valor']
        #conductorform  = form.cleaned_data['conductor']
        obacform  = form.cleaned_data['obac']
        fechaform  = form.cleaned_data['fecha']
        tarjeta_tctform  = form.cleaned_data['tarjeta_tct']

        # almacenamos el kilometraje y hodometro de la maquina
        maquina_id = int(self.request.POST.get('maquina'))
        maquina = Maquina.objects.get(pk=maquina_id)
        maquina.kilometraje = km_regresoform
        maquina.hodometro = hm_regresoform
        maquina.save()

        # Creamos un nuevo servicio
        compania_id = int(self.request.POST.get('compania'))
        conductor_id = int(self.request.POST.get('conductor'))
        compania_obj = Compania.objects.get(pk=compania_id)
        conductor_obj = Conductor.objects.get(pk=conductor_id)

        clave_obj = Clave.objects.get(nombre='6--14')
        servicio = Bitacora(compania=compania_obj,maquina=maquina,conductor=conductor_obj,direccion=servicentroform,
                            fecha=fechaform,hora_salida='00:00',hora_llegada='00:00',clave=clave_obj,
                            kilometraje_salida=km_salidaform,kilometraje_llegada=km_regresoform,
                            hodometro_salida=hm_salidaform,hodometro_llegada=hm_regresoform,
                            observciones='Carga combustible de '+ str(litrosform) +' litros, valor: $'+str(valorform)+', obac: '+obacform+', boucher TCT: '+str(tarjeta_tctform))
        servicio.save()

        return super(CombustibleCreateView, self).form_valid(form)

@method_decorator(login_required, name='dispatch')
class CombustibleListView(ListView):
    #model = Carguios_combustible
    template_name = 'combustible_list.html'

    def get_queryset(self):
        if (self.request.user.username == 'admin'):
            queryset = Carguios_combustible.objects.all()
        else:
            user_comp = self.request.user.usuariocomp.compania.pk
            queryset = Carguios_combustible.objects.filter(compania=user_comp)

        return queryset

combustible_create = CombustibleCreateView.as_view()
combustible_list = CombustibleListView.as_view()


class IndexView(TemplateView):
    template_name = "index.html"

index_view = IndexView.as_view()

class DashboardMaquinasListView(ListView):
    #queryset = Book.objects.filter(publisher__name='ACME Publishing')
    queryset = Maquina.objects.values('compania','nombre','venc_patente','hodometro','kilometraje')
    template_name = 'dashboard.html'

dashboard_maquina_list_view = DashboardMaquinasListView.as_view()