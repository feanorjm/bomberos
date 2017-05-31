from django.shortcuts import render
from maintenance.forms import BitacoraForm
from maintenance.models import Bitacora
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic import ListView
from django.views.generic.detail import DetailView

class BitacoraDetail(DetailView):
    model = Bitacora
    template_name = 'bitacora_detalle.html'

bitacora_detail = BitacoraDetail.as_view()

class BitacoraList(ListView):
    model = Bitacora
    template_name = 'bitacora_list.html'

bitacora_list = BitacoraList.as_view()

class BitacoraCreateView(CreateView):
    form_class = BitacoraForm
    template_name = 'bitacora.html'
    success_url = '/bitacora/add'

bitacora_create_view = BitacoraCreateView.as_view()