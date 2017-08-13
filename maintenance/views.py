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
from datetime import datetime, timedelta
from collections import OrderedDict
from django.db.models import Sum, F
from decimal import *

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
        today = datetime.now()
        if (self.request.user.usuariocomp.tipo in ('2','3')):
            queryset = Bitacora.objects.filter(fecha__month=today.month).order_by('-fecha')
        else:
            user_comp = self.request.user.usuariocomp.compania.pk
            queryset = Bitacora.objects.filter(compania=user_comp,fecha__month=today.month).order_by('-fecha')

        return queryset

    def get_context_data(self, **kwargs):
        context = super(BitacoraList, self).get_context_data(**kwargs)
        claves_list = Clave.objects.all()
        context['claves_list'] = claves_list
        return context

    def post(self, request, *args, **kwargs):
        today = datetime.now()
        fecha_ini = self.request.POST.get('fecha_ini')
        fecha_fin = self.request.POST.get('fecha_fin')
        clave = self.request.POST.get('clave')
        datos_list = {}

        if (fecha_ini != '' and fecha_fin != '' and clave != ''):
            clave_obj = Clave.objects.get(pk=clave)
            datos_list = {'fecha_ini':fecha_ini, 'fecha_fin':fecha_fin,'clave':clave_obj.pk}

            if (self.request.user.usuariocomp.tipo in ('2','3')):
                servicios = Bitacora.objects.filter(fecha__range=(fecha_ini,fecha_fin),clave=clave_obj).order_by('-fecha','-hora_salida')
            else:
                user_comp = self.request.user.usuariocomp.compania.pk
                servicios = Bitacora.objects.filter(compania=user_comp,fecha__range=(fecha_ini,fecha_fin),clave=clave_obj).order_by('-fecha','-hora_salida')

        elif (fecha_ini != '' and fecha_fin != ''):
            datos_list = {'fecha_ini':fecha_ini, 'fecha_fin':fecha_fin}
            if (self.request.user.usuariocomp.tipo in ('2','3')):
                servicios = Bitacora.objects.filter(fecha__range=(fecha_ini,fecha_fin)).order_by('-fecha','-hora_salida')
            else:
                user_comp = self.request.user.usuariocomp.compania.pk
                servicios = Bitacora.objects.filter(compania=user_comp,fecha__range=(fecha_ini,fecha_fin)).order_by('-fecha','-hora_salida')

        elif (clave != ''):
            clave_obj = Clave.objects.get(pk=clave)
            datos_list = {'clave':clave_obj.pk}

            if (self.request.user.usuariocomp.tipo in ('2','3')):
                servicios = Bitacora.objects.filter(clave=clave_obj).order_by('-fecha','-hora_salida')
            else:
                user_comp = self.request.user.usuariocomp.compania.pk
                servicios = Bitacora.objects.filter(compania=user_comp,clave=clave_obj).order_by('-fecha','-hora_salida')

        else:
            if (self.request.user.usuariocomp.tipo in ('2','3')):
                servicios = Bitacora.objects.filter(fecha__month=today.month).order_by('-fecha','-hora_salida')
            else:
                user_comp = self.request.user.usuariocomp.compania.pk
                servicios = Bitacora.objects.filter(compania=user_comp,fecha__month=today.month).order_by('-fecha','-hora_salida')

        context = {}
        claves_list = Clave.objects.all()
        context['claves_list'] = claves_list
        context['object_list'] = servicios
        context['datos_list'] = datos_list

        return render(request,self.template_name,context=context)



@method_decorator(login_required, name='dispatch')
class BitacoraCreateView(CreateView):
    form_class = BitacoraForm
    template_name = 'bitacora.html'
    #success_url = '/bitacora/add'

    def get_context_data(self, **kwargs):
        context = super(BitacoraCreateView, self).get_context_data(**kwargs)
        #context['username'] = self.request.user.username
        context['form'].fields['clave'].queryset = Clave.objects.exclude(nombre='6--14')

        if (self.request.user.usuariocomp.tipo in ('2','3')):
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

        if (self.request.user.usuariocomp.tipo in ('2','3')):
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
        if (self.request.user.usuariocomp.tipo in ('2','3')):
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
        hm_bomba_salidaform = form.cleaned_data['ho_bomba_salida']
        hm_bomba_regresoform = form.cleaned_data['ho_bomba_regreso']
        maquinaform = form.cleaned_data['maquina']
        maquina = Maquina.objects.get(nombre=maquinaform)
        maquina.kilometraje = kilometrajeform
        maquina.hodometro = hodometroform
        maquina.hodometro_bomba = hm_bomba_regresoform
        maquina.save()

        # obtenemos los datos de la cabecera de la matencion
        fechaform = form.cleaned_data['fecha']
        km_salidaform = form.cleaned_data['ki_salida']
        hm_salidaform = form.cleaned_data['ho_salida']
        km_regresoform = kilometrajeform
        hm_regresoform = hodometroform
        cod_manform = form.cleaned_data['cod_man']
        num_facturaform = form.cleaned_data['num_factura']
        valorform = form.cleaned_data['valor']
        tallerform = form.cleaned_data['taller']
        observacionform = form.cleaned_data['observacion']
        hora_salidaform = form.cleaned_data['hora_salida']
        hora_llegadaform = form.cleaned_data['hora_llegada']

        # Creamos un nuevo servicio
        compania_id = int(self.request.POST.get('compania'))
        conductor_id = int(self.request.POST.get('responsable'))
        compania_obj = Compania.objects.get(pk=compania_id)
        conductor_obj = Conductor.objects.get(pk=conductor_id)

        clave_obj = Clave.objects.get(nombre='6--13')
        servicio = Bitacora(compania=compania_obj, maquina=maquina, conductor=conductor_obj, direccion=tallerform,
                            fecha=fechaform, hora_salida=hora_salidaform, hora_llegada=hora_llegadaform, clave=clave_obj,
                            kilometraje_salida=km_salidaform, kilometraje_llegada=km_regresoform,
                            hodometro_salida=hm_salidaform, hodometro_llegada=hm_regresoform,
                            ho_bomba_salida=hm_bomba_salidaform, ho_bomba_regreso=hm_bomba_regresoform,
                            observciones='Mantencion orden de trabajo: '+ cod_manform + ', observacion:' + observacionform)
        servicio.save()
        self.object = form.save()

        mantencion_obj = self.object
        mantencion_obj.servicio = servicio
        mantencion_obj.save()

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

        ultimo_servicio = Bitacora.objects.filter(maquina__id=maquina).values('fecha').order_by('-fecha')[:1]
        print(ultimo_servicio)

        #conductores_maq = Conductor.objects.filter(maquina__nombre=maquina).values('id')
        print(parametros)
        return JsonResponse({'parametros': list(parametros), 'ultimo_servicio': list(ultimo_servicio)})


@method_decorator(login_required, name='dispatch')
class MantencionListView(ListView):
    #model = Mantencion
    template_name = 'mantencion_list.html'

    def get_queryset(self):
        if (self.request.user.usuariocomp.tipo in ('2','3')):
            queryset = Mantencion.objects.all().order_by('-fecha')
        else:
            user_comp = self.request.user.usuariocomp.compania.pk
            queryset = Mantencion.objects.filter(compania=user_comp).order_by('-fecha')

        return queryset


    def post(self, request, *args, **kwargs):
        today = datetime.now()
        fecha_ini = self.request.POST.get('fecha_ini')
        fecha_fin = self.request.POST.get('fecha_fin')
        datos_list = {}

        if (fecha_ini != '' and fecha_fin != ''):
            datos_list = {'fecha_ini':fecha_ini, 'fecha_fin':fecha_fin}

            if (self.request.user.usuariocomp.tipo in ('2','3')):
                mantenciones = Mantencion.objects.filter(fecha__range=(fecha_ini,fecha_fin)).order_by('-fecha')

            else:
                user_comp = self.request.user.usuariocomp.compania.pk
                mantenciones = Mantencion.objects.filter(compania=user_comp,fecha__range=(fecha_ini,fecha_fin)).order_by('-fecha')

        else:
            if (self.request.user.usuariocomp.tipo in ('2','3')):
                mantenciones = Mantencion.objects.all().order_by('-fecha')
            else:
                user_comp = self.request.user.usuariocomp.compania.pk
                mantenciones = Mantencion.objects.filter(compania=user_comp).order_by('-fecha')

        context = {}
        context['object_list'] = mantenciones
        context['datos_list'] = datos_list

        return render(request,self.template_name,context=context)


@method_decorator(login_required, name='dispatch')
class MantencionDetailView(DetailView):
    model = Mantencion
    template_name = 'mantencion_detalle.html'

    #DEFINIR EL CONTEXT DATA Y HACER QUERYSET Y BUSCAR LOS DATOS DEL DETALLE Y LOS REPUESTOS
    def get_context_data(self, *args, **kwargs):
        context = super(MantencionDetailView, self).get_context_data(*args, **kwargs)
        today = datetime.now()

        mantencion_obj = context['object']

        detalle_mantencion_list = DetalleMantencion.objects.filter(mantencion=mantencion_obj)
        repuesto_detalle_mantencion_list = RepuestoDetalleMantencion.objects.filter(mantencion=mantencion_obj)



        context['detalle_mantencion_list'] = detalle_mantencion_list
        context['repuesto_detalle_mantencion_list'] = repuesto_detalle_mantencion_list
        return context

class MantencionDeleteView(DeleteView):
    model = Mantencion
    template_name = 'mantencion_delete.html'
    success_url = reverse_lazy('mantencion_list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        servicio = self.object.servicio
        print(self.object,servicio)
        servicio.delete()

        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)


@method_decorator(login_required, name='dispatch')
class MantencionUpdateView(UpdateView):
    model = Mantencion
    form_class = MantencionForm
    template_name = 'mantencion_update.html'

    def form_valid(self, form):
        self.object = form.save()

        mantencion_obj = self.object

        # instanciamos el objeto Bitacora de referencia
        servicio = mantencion_obj.servicio

        # traemos los datos del formulario de Mantencion
        kilometrajeform = form.cleaned_data['ki_regreso']
        hodometroform = form.cleaned_data['ho_regreso']
        fechaform = form.cleaned_data['fecha']
        km_salidaform = form.cleaned_data['ki_salida']
        hm_salidaform = form.cleaned_data['ho_salida']
        km_regresoform = kilometrajeform
        hm_regresoform = hodometroform
        hm_bomba_salidaform = form.cleaned_data['ho_bomba_salida']
        hm_bomba_regresoform = form.cleaned_data['ho_bomba_regreso']
        cod_manform = form.cleaned_data['cod_man']
        num_facturaform = form.cleaned_data['num_factura']
        valorform = form.cleaned_data['valor']
        tallerform = form.cleaned_data['taller']
        observacionform = form.cleaned_data['observacion']
        hora_salidaform = form.cleaned_data['hora_salida']
        hora_llegadaform = form.cleaned_data['hora_llegada']


        maquina_id = int(self.request.POST.get('maquina'))
        maquina = Maquina.objects.get(pk=maquina_id)
        compania_id = int(self.request.POST.get('compania'))
        conductor_id = int(self.request.POST.get('responsable'))
        compania_obj = Compania.objects.get(pk=compania_id)
        conductor_obj = Conductor.objects.get(pk=conductor_id)

        servicio.compania = compania_obj
        servicio.maquina = maquina
        servicio.conductor = conductor_obj
        servicio.direccion = tallerform.razon_social
        servicio.fecha = fechaform
        servicio.kilometraje_salida = km_salidaform
        servicio.kilometraje_llegada = km_regresoform
        servicio.hodometro_salida = hm_salidaform
        servicio.hodometro_llegada = hm_regresoform
        servicio.ho_bomba_salida = hm_bomba_salidaform
        servicio.ho_bomba_regreso = hm_bomba_regresoform
        servicio.hora_salida = hora_salidaform
        servicio.hora_llegada = hora_llegadaform
        servicio.observciones = 'Mantencion orden de trabajo: '+ cod_manform + ', observacion:' + observacionform

        servicio.save()

        return super(MantencionUpdateView, self).form_valid(form)

mantencion_list = MantencionListView.as_view()
mantencion_detail = MantencionDetailView.as_view()
mantencion_delete = MantencionDeleteView.as_view()
mantencion_update = MantencionUpdateView.as_view()

#CRUD PARA MAQUINAS

@method_decorator(login_required, name='dispatch')
class MaquinaDetailView(DetailView):
    #context_object_name = "bitacora_detail"
    model = Maquina
    template_name = 'maquina_detail.html'


@method_decorator(login_required, name='dispatch')
class MaquinaListView(ListView):
    #model = Maquina
    template_name = 'maquina_list.html'

    def get_queryset(self):
        today = datetime.now()
        if (self.request.user.usuariocomp.tipo in ('2','3')):
            queryset = Maquina.objects.all().order_by('compania')
        else:
            user_comp = self.request.user.usuariocomp.compania.pk
            queryset = Maquina.objects.filter(compania=user_comp).order_by('compania')

        return queryset


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

@login_required
def get_all_conductores(request):
    if request.method == 'POST' and request.is_ajax():
        conductores_list = []
        conductores = Conductor.objects.all()
        for conductor in conductores:
            conductores_list.append({
                'id':conductor.id,
                'nombre':conductor.nombre.split(" ")[0]+" "+conductor.ap_paterno+" "+conductor.ap_materno,
            })
        print(conductores_list)

        return JsonResponse({'conductores': conductores_list})


#CRUD PARA CONDUCTORES

@method_decorator(login_required, name='dispatch')
class ConductorDetailView(DetailView):
    #context_object_name = "bitacora_detail"
    model = Conductor
    template_name = 'conductor_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ConductorDetailView, self).get_context_data(**kwargs)
        conductor = self.get_object()
        maquinas = Maquina.objects.filter(compania=conductor.compania)

        maquinas_list = ""
        for maquina in maquinas:
            if conductor in maquina.conductor.all():
                maquinas_list += maquina.nombre+"  "

        context['maquinas_list'] = maquinas_list


        return context



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
    #model = Conductor
    template_name = 'conductor_list.html'

    def get_queryset(self):
        today = datetime.now()
        if (self.request.user.usuariocomp.tipo in ('2','3')):
            queryset = Conductor.objects.all().order_by('compania','nombre')
        else:
            user_comp = self.request.user.usuariocomp.compania.pk
            queryset = Conductor.objects.filter(compania=user_comp).order_by('compania','nombre')

        return queryset

    def get_context_data(self, **kwargs):
        context = super(ConductorListView, self).get_context_data(**kwargs)
        companias_list = Compania.objects.all()
        if (self.request.user.usuariocomp.tipo not in ('2', '3')):
            user_comp = self.request.user.usuariocomp.compania.pk
            compania_obj = Compania.objects.get(pk=user_comp)
            companias_list = {compania_obj, }

        context['companias_list'] = companias_list
        return context

    def post(self, request, *args, **kwargs):
        compania = self.request.POST.get('compania')
        datos_list = {}
        context = {}

        companias_list = Compania.objects.all()

        if (compania != ''):
            compania_obj = Compania.objects.get(pk=compania)
            datos_list = {'compania':compania_obj.pk}
            if (self.request.user.usuariocomp.tipo in ('2','3')):
                conductores = Conductor.objects.filter(compania=compania_obj).order_by('compania','nombre')


            else:
                user_comp = self.request.user.usuariocomp.compania.pk
                conductores = Conductor.objects.filter(compania=user_comp).order_by('compania','nombre')
                companias_list = {compania_obj,}

        else:
            if (self.request.user.usuariocomp.tipo in ('2','3')):
                conductores = Conductor.objects.all().order_by('compania','nombre')
            else:
                user_comp = self.request.user.usuariocomp.compania.pk
                conductores = Conductor.objects.filter(compania=user_comp).order_by('compania','nombre')
                companias_list = {compania_obj, }

        context['companias_list'] = companias_list
        context['object_list'] = conductores
        context['datos_list'] = datos_list

        return render(request,self.template_name,context=context)

@method_decorator(login_required, name='dispatch')
class ConductorUpdateView(UpdateView):
    model = Conductor
    form_class = ConductorForm
    template_name = 'conductor_update.html'

@method_decorator(login_required, name='dispatch')
class ConductorDeleteView(DeleteView):
    model = Conductor
    template_name = 'conductor_delete.html'
    success_url = reverse_lazy('conductor_list')

conductor_list = ConductorListView.as_view()
conductor_detail = ConductorDetailView.as_view()
conductor_create = ConductorCreateView.as_view()
conductor_update = ConductorUpdateView.as_view()
conductor_delete = ConductorDeleteView.as_view()

#CRUD PARA CARGA COMBUSTIBLE

@method_decorator(login_required, name='dispatch')
class CombustibleCreateView(CreateView):
    form_class = CombustibleForm
    template_name = 'combustible_create.html'

    def get_success_url(self):
        return reverse("combustible_list")

    def get_context_data(self, **kwargs):
        context = super(CombustibleCreateView, self).get_context_data(**kwargs)
        if (self.request.user.usuariocomp.tipo in ('2','3')):
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
        hm_bomba_salidaform = form.cleaned_data['ho_bomba_salida']
        hm_bomba_regresoform = form.cleaned_data['ho_bomba_regreso']
        valorform  = form.cleaned_data['valor']
        #conductorform  = form.cleaned_data['conductor']
        obacform  = form.cleaned_data['obac']
        fechaform  = form.cleaned_data['fecha']
        tarjeta_tctform  = form.cleaned_data['tarjeta_tct']
        hora_salidaform = form.cleaned_data['hora_salida']
        hora_llegadaform = form.cleaned_data['hora_llegada']

        # almacenamos el kilometraje y hodometro de la maquina
        maquina_id = int(self.request.POST.get('maquina'))
        maquina = Maquina.objects.get(pk=maquina_id)
        maquina.kilometraje = km_regresoform
        maquina.hodometro = hm_regresoform
        maquina.hodometro_bomba = hm_bomba_regresoform
        maquina.save()

        # Creamos un nuevo servicio
        compania_id = int(self.request.POST.get('compania'))
        conductor_id = int(self.request.POST.get('conductor'))
        compania_obj = Compania.objects.get(pk=compania_id)
        conductor_obj = Conductor.objects.get(pk=conductor_id)

        clave_obj = Clave.objects.get(nombre='6--14')
        servicio = Bitacora(compania=compania_obj,maquina=maquina,conductor=conductor_obj,direccion=servicentroform,
                            fecha=fechaform,hora_salida=hora_salidaform,hora_llegada=hora_llegadaform,clave=clave_obj,
                            kilometraje_salida=km_salidaform,kilometraje_llegada=km_regresoform,
                            hodometro_salida=hm_salidaform,hodometro_llegada=hm_regresoform,
                            ho_bomba_salida=hm_bomba_salidaform,ho_bomba_regreso=hm_bomba_regresoform,
                            observciones='Carga combustible de '+ str(litrosform) +' litros, valor: $'+str(valorform)+', obac: '+obacform+', boucher TCT: '+str(tarjeta_tctform))
        servicio.save()
        self.object = form.save()

        combustible_obj = self.object
        combustible_obj.servicio = servicio
        combustible_obj.save()

        return super(CombustibleCreateView, self).form_valid(form)

@method_decorator(login_required, name='dispatch')
class CombustibleListView(ListView):
    #model = Carguios_combustible
    template_name = 'combustible_list.html'

    def get_queryset(self):
        if (self.request.user.usuariocomp.tipo in ('2','3')):
            queryset = Carguios_combustible.objects.all().order_by('-fecha')
        else:
            user_comp = self.request.user.usuariocomp.compania.pk
            queryset = Carguios_combustible.objects.filter(compania=user_comp).order_by('-fecha')

        print(queryset)

        return queryset

@method_decorator(login_required, name='dispatch')
class CombustibleDeleteView(DeleteView):
    model = Carguios_combustible
    template_name = 'combustible_delete.html'
    success_url = reverse_lazy('combustible_list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        servicio = self.object.servicio
        servicio.delete()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)

@method_decorator(login_required, name='dispatch')
class CombustibleDetailView(DetailView):
    #context_object_name = "bitacora_detail"
    model = Carguios_combustible
    template_name = 'combustible_detalle.html'

@method_decorator(login_required, name='dispatch')
class CombustibleUpdateView(UpdateView):

    # Esta clase no actualiza el kilometraje ni el hodometro, para no armar conflictos

    model = Carguios_combustible
    form_class = CombustibleForm
    template_name = 'combustible_update.html'

    def get_context_data(self, **kwargs):
        context = super(CombustibleUpdateView, self).get_context_data(**kwargs)
        if (self.request.user.usuariocomp.tipo in ('2','3')):
            context['form'].fields['compania'].queryset = Compania.objects.all()
        else:
            user_comp = self.request.user.usuariocomp.compania.pk
            context['form'].fields['compania'].queryset = Compania.objects.filter(pk=user_comp)
            #print(context)
        return context

    def form_valid(self, form):
        self.object = form.save()

        combustible_obj = self.object

        # instanciamos el objeto Bitacora de referencia
        servicio = combustible_obj.servicio

        #traemos los datos del formulario de Combustible
        litrosform = form.cleaned_data['litros']
        servicentroform = form.cleaned_data['servicentro']
        km_salidaform = form.cleaned_data['km_salida']
        hm_salidaform = form.cleaned_data['hm_salida']
        km_regresoform = form.cleaned_data['km_regreso']
        hm_regresoform = form.cleaned_data['hm_regreso']
        hm_bomba_salidaform = form.cleaned_data['ho_bomba_salida']
        hm_bomba_regresoform = form.cleaned_data['ho_bomba_regreso']
        valorform = form.cleaned_data['valor']
        obacform = form.cleaned_data['obac']
        fechaform = form.cleaned_data['fecha']
        tarjeta_tctform = form.cleaned_data['tarjeta_tct']
        hora_salidaform = form.cleaned_data['hora_salida']
        hora_llegadaform = form.cleaned_data['hora_llegada']

        maquina_id = int(self.request.POST.get('maquina'))
        maquina = Maquina.objects.get(pk=maquina_id)
        compania_id = int(self.request.POST.get('compania'))
        conductor_id = int(self.request.POST.get('conductor'))
        compania_obj = Compania.objects.get(pk=compania_id)
        conductor_obj = Conductor.objects.get(pk=conductor_id)

        servicio.compania = compania_obj
        servicio.maquina = maquina
        servicio.conductor = conductor_obj
        servicio.direccion = servicentroform.nombre + " - " + servicentroform.direccion
        servicio.fecha = fechaform
        servicio.kilometraje_salida = km_salidaform
        servicio.kilometraje_llegada = km_regresoform
        servicio.hodometro_salida = hm_salidaform
        servicio.hodometro_llegada = hm_regresoform
        servicio.ho_bomba_salida = hm_bomba_salidaform
        servicio.ho_bomba_regreso = hm_bomba_regresoform
        servicio.hora_salida = hora_salidaform
        servicio.hora_llegada = hora_llegadaform
        servicio.observciones = 'Carga combustible de ' + str(litrosform) + ' litros, valor: $' + \
                                str(valorform) + ', obac: ' + obacform + ', boucher TCT: ' + str(tarjeta_tctform)

        servicio.save()

        return super(CombustibleUpdateView, self).form_valid(form)


combustible_create = CombustibleCreateView.as_view()
combustible_list = CombustibleListView.as_view()
combustible_delete = CombustibleDeleteView.as_view()
combustible_detail = CombustibleDetailView.as_view()
combustible_update = CombustibleUpdateView.as_view()


class IndexView(TemplateView):
    template_name = "index.html"

index_view = IndexView.as_view()

class DashboardListView(ListView):
    #queryset = Book.objects.filter(publisher__name='ACME Publishing')
    #queryset = Maquina.objects.values('compania','nombre','venc_patente','hodometro','kilometraje')
    template_name = 'dashboard.html'

    def get_queryset(self):
        if (self.request.user.usuariocomp.tipo in ('2','3')):
            queryset = Maquina.objects.values('compania__nombre','nombre','venc_rev_tec',
                                              'hodometro','kilometraje','tiene_bomba',
                                              'hodometro_bomba').order_by('compania','nombre')
        else:
            user_comp = self.request.user.usuariocomp.compania.pk
            queryset = Maquina.objects.values('compania__nombre','nombre','venc_rev_tec',
                                              'hodometro','kilometraje','tiene_bomba',
                                              'hodometro_bomba').filter(compania=user_comp)

        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super(DashboardListView, self).get_context_data(*args, **kwargs)
        today = datetime.now()
        ranking_list = []
        if (self.request.user.usuariocomp.tipo in ('2','3')):
            query = Bitacora.objects.filter(fecha__year=today.year).\
                values('compania__nombre','conductor__nombre','conductor__ap_paterno','conductor__ap_materno').\
                annotate(horas=Sum(F('hodometro_llegada')-F('hodometro_salida'))).order_by('compania')

            for ranking in query:
                ranking_list.append({
                    'compania': ranking['compania__nombre'],
                    'conductor': ranking['conductor__nombre'].split(" ")[0]+" "+ranking['conductor__ap_paterno']+" "+ranking['conductor__ap_materno'],
                    'horas': ranking['horas'],
                })

            mantencion_list = DetalleMantencion.objects.filter(tipo_mantencion__nombre='Preventiva').\
                values('mantencion__maquina__nombre','division__nombre','subdivision__nombre',
                       'servicio__nombre','hodometro_prox_man','mantencion__fecha')

        else:
            user_comp = self.request.user.usuariocomp.compania.pk
            query = Bitacora.objects.filter(fecha__year=today.year,compania=user_comp). \
                values('compania__nombre', 'conductor__nombre', 'conductor__ap_paterno','conductor__ap_materno'). \
                annotate(horas=Sum(F('hodometro_llegada') - F('hodometro_salida'))).order_by('compania')

            for ranking in query:
                ranking_list.append({
                    'compania': ranking['compania__nombre'],
                    'conductor': ranking['conductor__nombre'].split(" ")[0]+" "+ranking['conductor__ap_paterno']+" "+ranking['conductor__ap_materno'],
                    'horas': ranking['horas'],
                })

            mantencion_list = DetalleMantencion.objects.filter(tipo_mantencion__nombre='Preventiva',mantencion__compania=user_comp). \
                values('mantencion__compania__nombre','mantencion__maquina__nombre', 'division__nombre', 'subdivision__nombre',
                       'servicio__nombre', 'hodometro_prox_man','mantencion__fecha')

        context['ranking_list'] = ranking_list
        context['mantencion_list'] = mantencion_list
        return context

dashboard_list_view = DashboardListView.as_view()

class ReporteCombustibleListView(ListView):
    template_name = 'reporte_combustible.html'

    def get_queryset(self):
        list_object = []

        queryset = list_object

        return queryset


    def get_context_data(self, **kwargs):
        context = super(ReporteCombustibleListView, self).get_context_data(**kwargs)
        today = datetime.now()
        mes_ant_12 = today - timedelta(days=365)
        dates = [mes_ant_12.strftime("%Y-%m-%d"), today.strftime("%Y-%m-%d")]
        start, end = [datetime.strptime(_, "%Y-%m-%d") for _ in dates]
        meses_list = OrderedDict(((start + timedelta(_)).strftime(r"%m-%Y"), None) for _ in reversed(range((end - start).days))).keys()

        context['meses_list'] = meses_list

        if (self.request.user.usuariocomp.tipo in ('2', '3')):
            companias_list = Compania.objects.all()
            context['companias_list'] = companias_list
            context['object_list'] = {}
            compania_obj = Compania.objects.all().order_by('id')[:1][0]
            maquinas_list = Maquina.objects.filter(compania=compania_obj)
            context['maquinas_list'] = maquinas_list

        else:
            user_comp = self.request.user.usuariocomp.compania.pk
            compania_obj = Compania.objects.get(pk=user_comp)
            maquina_obj = Maquina.objects.filter(compania=compania_obj).order_by('id')[:1][0]
            datos_list = {'maquina': maquina_obj.pk, 'nombre': maquina_obj.nombre, 'patente': maquina_obj.patente,
                          'mes': str(today.month) + " - " + str(today.year)}
            #print(maquina_obj)
            context['datos_list'] = datos_list
            maquinas_list = Maquina.objects.filter(compania=compania_obj)
            context['maquinas_list'] = maquinas_list


        return context

    def post(self, request, *args, **kwargs):
        today = datetime.now()
        mes_ant_12 = today - timedelta(days=365)
        dates = [mes_ant_12.strftime("%Y-%m-%d"), today.strftime("%Y-%m-%d")]
        start, end = [datetime.strptime(_, "%Y-%m-%d") for _ in dates]
        meses_list = OrderedDict(((start + timedelta(_)).strftime(r"%m-%Y"), None) for _ in reversed(range((end - start).days))).keys()
        context = {}
        context['meses_list'] = meses_list

        clave_obj = Clave.objects.get(nombre='6--14')
        maquina_id = request.POST.get('maquina')
        mes = request.POST.get('mes')
        mes_sel = int(mes.split("-")[0])
        year_sel = int(mes.split("-")[1])
        datos_list = {}

        if (maquina_id != ''):
            if (self.request.user.usuariocomp.tipo in ('2', '3')):
                companias_list = Compania.objects.all()
                context['companias_list'] = companias_list
                compania_id = self.request.POST.get('compania')
                compania_obj = Compania.objects.get(pk=compania_id)
                maquinas_list = Maquina.objects.filter(compania=compania_obj)
                maquina_obj = Maquina.objects.get(pk=maquina_id)
                #context['maquinas_list'] = maquinas_list
                datos_list = {'compania': compania_obj.pk, 'maquina': maquina_obj.pk, 'nombre': maquina_obj.nombre, 'patente': maquina_obj.patente,
                              'mes': mes}
            else:
                user_comp = self.request.user.usuariocomp.compania.pk
                compania_obj = Compania.objects.get(pk=user_comp)
                maquina_obj = Maquina.objects.get(pk=maquina_id)
                maquinas_list = Maquina.objects.filter(compania=compania_obj).order_by('id')
                datos_list = {'maquina':maquina_obj.pk, 'nombre':maquina_obj.nombre, 'patente':maquina_obj.patente, 'mes': mes}


            maquina_default = maquina_obj

            servicios = Bitacora.objects.filter(maquina=maquina_default, fecha__month=mes_sel,fecha__year=year_sel).order_by('id')

            list_object = []

            petroleo_anterior = Decimal(140)

            km_diferencia_total = 0
            consumo_motor_total = 0

            if len(servicios) > 0:
                for servicio in servicios:
                    maquina = servicio.maquina
                    # petroleo
                    petroleo_colocado = Decimal(0)
                    if (servicio.clave.id == clave_obj.id):
                        carga = Carguios_combustible.objects.get(servicio=servicio)
                        petroleo_colocado = Decimal(carga.litros)

                    # kilometraje
                    kilometraje_anterior = servicio.kilometraje_salida
                    kilometraje_actual = servicio.kilometraje_llegada
                    kilometraje_diferencia = kilometraje_actual - kilometraje_anterior
                    km_diferencia_total += kilometraje_diferencia

                    # horas motor
                    horas_motor_anterior = servicio.hodometro_salida
                    horas_motor_actual = servicio.hodometro_llegada
                    horas_motor_diferencia = horas_motor_actual - horas_motor_anterior

                    # horas bomba
                    if (maquina.tiene_bomba == True):
                        print(maquina)
                        horas_bomba_anterior = servicio.ho_bomba_salida
                        horas_bomba_actual = servicio.ho_bomba_regreso
                        horas_bomba_diferencia = horas_bomba_actual - horas_bomba_anterior
                    else:
                        horas_bomba_anterior = 0
                        horas_bomba_actual = 0
                        horas_bomba_diferencia = 0


                    # calculo de litros
                    consumo_bomba = (horas_bomba_actual - horas_bomba_anterior) * 10
                    consumo_motor = round(float(kilometraje_diferencia) / float(1.4), 2)
                    consumo_motor_total += consumo_motor

                    petroleo_consumo = Decimal(round(consumo_bomba + Decimal(consumo_motor), 1))

                    petroleo_actual = Decimal(round(petroleo_anterior - petroleo_consumo + petroleo_colocado, 1))
                    #rendimiento = Decimal(round(float(kilometraje_diferencia) / float(consumo_motor), 1))

                    # otros datos
                    fecha_dia = servicio.fecha.day
                    servicio_id = servicio.id
                    clave = servicio.clave.nombre
                    direccion = servicio.direccion
                    conductor = servicio.conductor

                    list_query = {'num': servicio_id,
                                  'fecha_dia': fecha_dia,
                                  'clave': clave,
                                  'direccion': direccion,

                                  'petroleo_anterior': petroleo_anterior,
                                  'petroleo_colocado': petroleo_colocado,
                                  'petroleo_consumo': petroleo_consumo,
                                  'petroleo_actual': petroleo_actual,

                                  'km_anterior': kilometraje_anterior,
                                  'km_actual': kilometraje_actual,
                                  'km_dif': kilometraje_diferencia,

                                  'bomba_anterior': horas_bomba_anterior,
                                  'bomba_actual': horas_bomba_actual,
                                  'bomba_dif': horas_bomba_diferencia,

                                  'motor_anterior': horas_motor_anterior,
                                  'motor_actual': horas_motor_actual,
                                  'motor_dif': horas_motor_diferencia,

                                  'conductor': conductor
                                  }

                    list_object.append(list_query)

                    petroleo_anterior = petroleo_actual

                if (consumo_motor_total == 0):
                    rendimiento = "Indeterminado"
                else:
                    rendimiento = round(float(km_diferencia_total) / float(consumo_motor_total),2)

                datos_list['km_diferencia_total'] = km_diferencia_total
                datos_list['consumo_motor_total'] = consumo_motor_total
                datos_list['rendimiento'] = rendimiento


            else:
                list_object = []
                if (self.request.user.usuariocomp.tipo in ('2', '3')):
                    datos_list = {'mensaje': 'No exiten datos para la Máquina solicitada','compania': compania_obj.pk, 'maquina':maquina_obj.pk, 'mes':mes}
                else:
                    datos_list = {'mensaje': 'No exiten datos para la Máquina solicitada', 'maquina': maquina_obj.pk, 'mes':mes}





        context['maquinas_list'] = maquinas_list
        context['object_list'] = list_object
        context['datos_list'] = datos_list


        return render(request,self.template_name,context=context)

reporte_combustible_list_view = ReporteCombustibleListView.as_view()

def get_maquinas_compania(request):
    if request.method == 'POST' and request.is_ajax():
        compania = request.POST.get('compania')
        maquinas = Maquina.objects.filter(compania=compania).values('id','nombre')
        return JsonResponse({'maquinas': list(maquinas)})


class ReporteMaquinistasListView(ListView):
    template_name = 'reporte_maquinistas.html'

    def get_queryset(self):
        list_object = []

        queryset = list_object

        return queryset

    def get_context_data(self, **kwargs):
        context = super(ReporteMaquinistasListView, self).get_context_data(**kwargs)
        today = datetime.now()
        if (self.request.user.usuariocomp.tipo in ('2', '3')):
            companias_list = Compania.objects.all()
            context['companias_list'] = companias_list

        else:
            user_comp = self.request.user.usuariocomp.compania.pk
            compania_obj = Compania.objects.get(pk=user_comp)
            #datos_list = {'maquina': maquina_obj.pk, 'nombre': maquina_obj.nombre, 'patente': maquina_obj.patente,'mes': str(today.month) + " - " + str(today.year)}
            #print(maquina_obj)
            #context['datos_list'] = datos_list

        context['object_list'] = {}


        return context

    def post(self, request, *args, **kwargs):
        today = datetime.now()
        compania_id = self.request.POST.get('compania')
        fecha_ini = self.request.POST.get('fecha_ini')
        fecha_fin = self.request.POST.get('fecha_fin')

        context = {}

        if (self.request.user.usuariocomp.tipo in ('2', '3') and compania_id != ''):

            companias_list = Compania.objects.all()
            context['companias_list'] = companias_list
            compania_id = self.request.POST.get('compania')
            compania_obj = Compania.objects.get(pk=compania_id)
            datos_list = {'fecha_ini': fecha_ini, 'fecha_fin': fecha_fin, 'compania':compania_obj.pk}
        else:
            user_comp = self.request.user.usuariocomp.compania.pk
            compania_obj = Compania.objects.get(pk=user_comp)
            datos_list = {'fecha_ini': fecha_ini, 'fecha_fin': fecha_fin, }


        maquinistas = Conductor.objects.filter(compania=compania_obj).order_by('id')
        maquinas = Maquina.objects.filter(compania=compania_obj).order_by('id')

        list_object = []

        if len(maquinistas) > 0:
            for maquinista in maquinistas:
                horas = []
                horas_totales = 0
                for maquina in maquinas:
                    servicios = Bitacora.objects.filter(maquina=maquina,conductor=maquinista,fecha__range=(fecha_ini,fecha_fin)).order_by('id')
                    horas_manejadas = 0
                    for servicio in servicios:
                        horas_manejadas += servicio.hodometro_llegada - servicio.hodometro_salida

                    horas_totales += horas_manejadas

                    horas.append({'maquina':maquina.nombre,'horas':horas_manejadas})
                nombre = maquinista.nombre.split(" ")
                maquinista_list =  {'compania':maquinista.compania.nombre,
                                    'nombre':nombre[0]+ " " + maquinista.ap_paterno + " " + maquinista.ap_materno,
                                    'rut':maquinista.rut,
                                    'venc':maquinista.venc_lic,
                                    'horas':horas,
                                    'total':horas_totales}

                list_object.append(maquinista_list)


        context['object_list'] = list_object
        context['maquinas_list'] = maquinas
        context['datos_list'] = datos_list


        return render(request,self.template_name,context=context)

reporte_maquinistas_list_view = ReporteMaquinistasListView.as_view()

class ReporteServiciosListView(ListView):
    template_name = 'reporte_servicios.html'

    def get_queryset(self):
        list_object = []

        queryset = list_object

        return queryset

    def get_context_data(self, **kwargs):
        context = super(ReporteServiciosListView, self).get_context_data(**kwargs)
        today = datetime.now()

        if (self.request.user.usuariocomp.tipo in ('2', '3')):
            companias_list = Compania.objects.all()
            context['companias_list'] = companias_list
            compania_obj = Compania.objects.all().order_by('id')[:1][0]
            maquinas_list = Maquina.objects.filter(compania=compania_obj)
            context['maquinas_list'] = maquinas_list

        else:
            user_comp = self.request.user.usuariocomp.compania.pk
            compania_obj = Compania.objects.get(pk=user_comp)
            #datos_list = {'maquina': maquina_obj.pk, 'nombre': maquina_obj.nombre, 'patente': maquina_obj.patente,'mes': str(today.month) + " - " + str(today.year)}
            #print(maquina_obj)
            #context['datos_list'] = datos_list
            maquinas_list = Maquina.objects.filter(compania=compania_obj)
            context['maquinas_list'] = maquinas_list

        context['object_list'] = {}


        return context

    def post(self, request, *args, **kwargs):
        today = datetime.now()
        compania_id = self.request.POST.get('compania')
        maquina_id = self.request.POST.get('maquina')
        fecha_ini = self.request.POST.get('fecha_ini')
        fecha_fin = self.request.POST.get('fecha_fin')

        context = {}

        if int(maquina_id) != 0:
            if (self.request.user.usuariocomp.tipo in ('2', '3') and compania_id != ''):

                companias_list = Compania.objects.all()
                context['companias_list'] = companias_list
                compania_obj = Compania.objects.get(pk=compania_id)
                maquina_obj = Maquina.objects.get(pk=maquina_id)
                datos_list = {'fecha_ini': fecha_ini, 'fecha_fin': fecha_fin, 'compania':compania_obj.pk, 'maquina':maquina_obj.pk}
                maquinas_list = Maquina.objects.filter(compania=compania_obj)
                context['maquinas_list'] = maquinas_list
            else:
                user_comp = self.request.user.usuariocomp.compania.pk
                compania_obj = Compania.objects.get(pk=user_comp)
                maquina_obj = Maquina.objects.get(pk=maquina_id)
                datos_list = {'fecha_ini': fecha_ini, 'fecha_fin': fecha_fin, 'maquina':maquina_obj.pk,}
                maquinas_list = Maquina.objects.filter(compania=compania_obj)
                context['maquinas_list'] = maquinas_list

            if (fecha_ini == "" and fecha_fin == ""):
                servicios = Bitacora.objects.filter(compania=compania_obj, maquina=maquina_obj,fecha__month=today.month).order_by('fecha')
            else:
                servicios = Bitacora.objects.filter(compania=compania_obj,maquina=maquina_obj, fecha__range=(fecha_ini,fecha_fin)).order_by('fecha')

        else:
            if (self.request.user.usuariocomp.tipo in ('2', '3') and compania_id != ''):

                companias_list = Compania.objects.all()
                context['companias_list'] = companias_list
                compania_obj = Compania.objects.get(pk=compania_id)
                datos_list = {'fecha_ini': fecha_ini, 'fecha_fin': fecha_fin, 'compania':compania_obj.pk, 'maquina':0}
                maquinas_list = Maquina.objects.filter(compania=compania_obj)
                context['maquinas_list'] = maquinas_list
            else:
                user_comp = self.request.user.usuariocomp.compania.pk
                compania_obj = Compania.objects.get(pk=user_comp)
                datos_list = {'fecha_ini': fecha_ini, 'fecha_fin': fecha_fin, 'maquina':0,}
                maquinas_list = Maquina.objects.filter(compania=compania_obj)
                context['maquinas_list'] = maquinas_list

            if (fecha_ini == "" and fecha_fin == ""):
                servicios = Bitacora.objects.filter(compania=compania_obj,fecha__month=today.month).order_by('fecha')
            else:
                servicios = Bitacora.objects.filter(compania=compania_obj, fecha__range=(fecha_ini,fecha_fin)).order_by('fecha')

        list_object = []

        if len(servicios) > 0:
            for servicio in servicios:
                servicio_list =  {'id':servicio.pk,
                                  'maquina':servicio.maquina.nombre,
                                  'clave':servicio.clave.nombre,
                                  'fecha':servicio.fecha,
                                  'direccion':servicio.direccion,
                                  'despacho':servicio.hora_salida,
                                  'km_salida': servicio.kilometraje_salida,
                                  'km_llegada':servicio.kilometraje_llegada,
                                  'conductor':servicio.conductor
                                  }

                list_object.append(servicio_list)


        context['object_list'] = list_object
        context['datos_list'] = datos_list


        return render(request,self.template_name,context=context)

reporte_servicios_list_view = ReporteServiciosListView.as_view()

class ReporteMantencionesListView(ListView):
    template_name = 'reporte_mantenciones.html'

    def get_queryset(self):
        list_object = []

        queryset = list_object

        return queryset

    def get_context_data(self, **kwargs):
        context = super(ReporteMantencionesListView, self).get_context_data(**kwargs)
        today = datetime.now()

        if (self.request.user.usuariocomp.tipo in ('2', '3')):
            companias_list = Compania.objects.all()
            context['companias_list'] = companias_list

        else:
            user_comp = self.request.user.usuariocomp.compania.pk
            compania_obj = Compania.objects.get(pk=user_comp)
            #datos_list = {'maquina': maquina_obj.pk, 'nombre': maquina_obj.nombre, 'patente': maquina_obj.patente,'mes': str(today.month) + " - " + str(today.year)}
            #print(maquina_obj)
            #context['datos_list'] = datos_list

        context['object_list'] = {}


        return context

    def post(self, request, *args, **kwargs):
        today = datetime.now()
        compania_id = self.request.POST.get('compania')
        fecha_ini = self.request.POST.get('fecha_ini')
        fecha_fin = self.request.POST.get('fecha_fin')

        context = {}

        if (self.request.user.usuariocomp.tipo in ('2', '3') and compania_id != ''):

            companias_list = Compania.objects.all()
            context['companias_list'] = companias_list
            compania_obj = Compania.objects.get(pk=compania_id)
            datos_list = {'fecha_ini': fecha_ini, 'fecha_fin': fecha_fin, 'compania':compania_obj.pk}
        else:
            user_comp = self.request.user.usuariocomp.compania.pk
            compania_obj = Compania.objects.get(pk=user_comp)
            datos_list = {'fecha_ini': fecha_ini, 'fecha_fin': fecha_fin}

        if (fecha_ini == "" and fecha_fin == ""):
            mantenciones = DetalleMantencion.objects.filter(mantencion__compania=compania_obj,mantencion__fecha__month=today.month).order_by('mantencion__fecha')
        else:
            mantenciones = DetalleMantencion.objects.filter(mantencion__compania=compania_obj, mantencion__fecha__range=(fecha_ini,fecha_fin)).order_by('mantencion__fecha')


        list_object = []

        if len(mantenciones) > 0:
            for detalle in mantenciones:
                if detalle.servicio == None:
                    detalle_Servicio = "No especificado"
                else:
                    detalle_Servicio = detalle.servicio.nombre
                detalle_list =  {
                    'fecha':detalle.mantencion.fecha,
                    'taller': detalle.mantencion.taller.razon_social,
                    'maquina': detalle.mantencion.maquina,
                    'division':detalle.division.nombre,
                    'subdivision':detalle.subdivision.nombre,
                    'servicio':detalle_Servicio,
                    'tipo_mantencion':detalle.tipo_mantencion.nombre,
                    'factura': detalle.mantencion.num_factura,
                    'valor': detalle.mantencion.valor,
                }

                list_object.append(detalle_list)


        context['object_list'] = list_object
        context['datos_list'] = datos_list


        return render(request,self.template_name,context=context)

reporte_mantenciones_list_view = ReporteMantencionesListView.as_view()

class ReporteTalleresListView(ListView):
    template_name = 'reporte_talleres.html'

    def get_queryset(self):
        list_object = []

        queryset = list_object

        return queryset

    def get_context_data(self, **kwargs):
        context = super(ReporteTalleresListView, self).get_context_data(**kwargs)
        today = datetime.now()

        if (self.request.user.usuariocomp.tipo in ('2', '3')):
            companias_list = Compania.objects.all()
            context['companias_list'] = companias_list

        else:
            user_comp = self.request.user.usuariocomp.compania.pk
            compania_obj = Compania.objects.get(pk=user_comp)
            #datos_list = {'maquina': maquina_obj.pk, 'nombre': maquina_obj.nombre, 'patente': maquina_obj.patente,'mes': str(today.month) + " - " + str(today.year)}
            #print(maquina_obj)
            #context['datos_list'] = datos_list

        context['object_list'] = {}


        return context

    def post(self, request, *args, **kwargs):
        today = datetime.now()
        compania_id = self.request.POST.get('compania')
        fecha_ini = self.request.POST.get('fecha_ini')
        fecha_fin = self.request.POST.get('fecha_fin')

        context = {}

        if (self.request.user.usuariocomp.tipo in ('2', '3') and compania_id != ''):

            companias_list = Compania.objects.all()
            context['companias_list'] = companias_list
            compania_obj = Compania.objects.get(pk=compania_id)
            datos_list = {'fecha_ini': fecha_ini, 'fecha_fin': fecha_fin, 'compania':compania_obj.pk}
        else:
            user_comp = self.request.user.usuariocomp.compania.pk
            compania_obj = Compania.objects.get(pk=user_comp)
            datos_list = {'fecha_ini': fecha_ini, 'fecha_fin': fecha_fin}

        maquinas = Maquina.objects.filter(compania=compania_obj)

        mantenciones_total = []
        costo_total = 0

        for maquina in maquinas:
            if (fecha_ini == "" and fecha_fin == ""):
                mantenciones = Mantencion.objects.filter(maquina=maquina, fecha__month=today.month).values('maquina__nombre','taller__razon_social').annotate(total=Sum('valor'))


            else:
                mantenciones = Mantencion.objects.filter(maquina=maquina, fecha__range=(fecha_ini,fecha_fin)).values('maquina__nombre','taller__razon_social').annotate(total=Sum('valor'))

            for mantencion in mantenciones:
                mantenciones_total.append({'maquina':mantencion['maquina__nombre'],
                                           'taller':mantencion['taller__razon_social'],
                                           'total': mantencion['total'],
                                           })
                costo_total += int(mantencion['total'])

        datos_list['costo_total'] = costo_total

        context['object_list'] = mantenciones_total
        context['datos_list'] = datos_list


        return render(request,self.template_name,context=context)

reporte_talleres_list_view = ReporteTalleresListView.as_view()