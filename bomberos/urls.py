from django.conf.urls import url, include
from django.contrib import admin
from bomberos.views import login_view,logout_view
from maintenance.views import (bitacora_create_view, bitacora_list, bitacora_detail, bitacora_update, bitacora_delete,
                               mantencion_create, mantencion_add_detalle, mantencion_add_repuesto,mantencion_list,mantencion_detail)

urlpatterns = [
    url(r'^chaining/', include('smart_selects.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', login_view,name='login_view'),
    url(r'^logout/$', logout_view, name='logout_view'),
    url(r'^bitacora/add/$', bitacora_create_view, name='bitacora_create_view'),
    url(r'^bitacora/$', bitacora_list, name='bitacora_list'),
    url(r'^bitacora/detalle/(?P<pk>\d+)$', bitacora_detail, name='bitacora_detail'),
    url(r'^bitacora/editar/(?P<pk>\d+)$', bitacora_update, name='bitacora_update'),
    url(r'^bitacora/eliminar/(?P<pk>\d+)$', bitacora_delete, name='bitacora_delete'),
    url(r'^mantencion/add/$', mantencion_create, name='mantencion_create'),
    url(r'^mantencion/add_detalle/$', mantencion_add_detalle, name='mantencion_add_detalle'),
    url(r'^mantencion/add_repuesto/$', mantencion_add_repuesto, name='mantencion_add_repuesto'),
    url(r'^mantenciones/$', mantencion_list, name='mantencion_list'),
    url(r'^mantencion/detalle/(?P<pk>\d+)$', mantencion_detail, name='mantencion_detail'),
]
