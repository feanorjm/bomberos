from django.shortcuts import render
from maintenance.forms import BitacoraForm
from maintenance.models import Bitacora
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse
from django.urls import reverse_lazy

class BitacoraDetail(DetailView):
    #context_object_name = "bitacora_detail"
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
    #success_url = '/bitacora/add'
    def get_success_url(self):
        return reverse("bitacora_list")

bitacora_create_view = BitacoraCreateView.as_view()

class BitacoraUpdateView(UpdateView):
    model = Bitacora
    form_class = BitacoraForm
    template_name = 'bitacora_update.html'

bitacora_update = BitacoraUpdateView.as_view()

class BitacoraDelete(DeleteView):
    model = Bitacora
    template_name = 'bitacora_delete.html'
    success_url = reverse_lazy('bitacora_list')

bitacora_delete = BitacoraDelete.as_view()