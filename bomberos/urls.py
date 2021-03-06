from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from bomberos.views import login_view,logout_view
from maintenance.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^chaining/', include('smart_selects.urls')),
    url(r'^$', bitacora_list,name='bitacora_list'),
    url(r'^index/$', bitacora_list,name='bitacora_list'),
    #url(r'^index/$', index_view,name='index_view'),
    url(r'^login/$', login_view,name='login_view'),
    url(r'^logout/$', logout_view, name='logout_view'),
    #BITACORA
    url(r'^bitacora/add/$', bitacora_create_view, name='bitacora_create_view'),
    url(r'^bitacora/$', bitacora_list, name='bitacora_list'),
    url(r'^bitacora/detalle/(?P<pk>\d+)$', bitacora_detail, name='bitacora_detail'),
    url(r'^bitacora/editar/(?P<pk>\d+)$', bitacora_update, name='bitacora_update'),
    url(r'^bitacora/eliminar/(?P<pk>\d+)$', bitacora_delete, name='bitacora_delete'),
    #MANTENCIONES
    #url(r'^mantencion/add/$', mantencion_create, name='mantencion_create'),
    url(r'^mantencion/add/$', mantencion_create_view, name='mantencion_create_view'),
    url(r'^mantencion/add/nuevo', mantencion_form_view, name='mantencion_form_view'),
    url(r'^mantencion/add/detalle$', detalle_mantencion_form_view, name='detalle_mantencion_form_view'),
    url(r'^mantencion/add/repuesto$', repuesto_detalle_mantencion_form_view, name='repuesto_detalle_mantencion_form_view'),
    #url(r'^mantencion/add_detalle/$', mantencion_add_detalle, name='mantencion_add_detalle'),
    #url(r'^mantencion/add_repuesto/$', mantencion_add_repuesto, name='mantencion_add_repuesto'),
    url(r'^mantenciones/$', mantencion_list, name='mantencion_list'),
    url(r'^mantencion/detalle/(?P<pk>\d+)$', mantencion_detail, name='mantencion_detail'),
    url(r'^mantencion/eliminar/(?P<pk>\d+)$', mantencion_delete, name='mantencion_delete'),
    url(r'^mantencion/editar/(?P<pk>\d+)$', mantencion_update, name='mantencion_update'),
    #MAQUINA
    url(r'^maquina/detalle/(?P<pk>\d+)$', maquina_detail, name='maquina_detail'),
    url(r'^maquinas/$', maquina_list, name='maquina_list'),
    url(r'^maquina/add/$', maquina_create, name='maquina_create'),
    url(r'^maquina/editar/(?P<pk>\d+)$', maquina_update, name='maquina_update'),
    url(r'^maquina/eliminar/(?P<pk>\d+)$', maquina_delete, name='maquina_delete'),
    url(r'^get_maquina_conductores/$', get_maquina_conductores, name='get_maquina_conductores'),
    url(r'^get_parametros_maquina/$', get_parametros_maquina, name='get_parametros_maquina'),

    #CONDUCTORES
    url(r'^conductores/$', conductor_list, name='conductor_list'),
    url(r'^conductor/detalle/(?P<pk>\d+)$', conductor_detail, name='conductor_detail'),
    url(r'^conductor/add/$', conductor_create, name='conductor_create'),
    url(r'^conductor/editar/(?P<pk>\d+)$', conductor_update, name='conductor_update'),
    url(r'^conductor/eliminar/(?P<pk>\d+)$', conductor_delete, name='conductor_delete'),

    #COMBUSTIBLE
    url(r'^combustible/add/$', combustible_create, name='combustible_create'),
    url(r'^carga-combustible/$', combustible_list, name='combustible_list'),
    url(r'^carga-combustible/eliminar/(?P<pk>\d+)$', combustible_delete, name='combustible_delete'),
    url(r'^carga-combustible/detalle/(?P<pk>\d+)$', combustible_detail, name='combustible_detail'),
    url(r'^carga-combustible/editar/(?P<pk>\d+)$', combustible_update, name='combustible_update'),

    #DASHBOARD
    url(r'^dashboard/$', dashboard_list_view, name='dashboard_list_view'),

    #REPORTES
    url(r'^reporte/parte-combustible/$', reporte_combustible_list_view, name='reporte_combustible_list_view'),
    url(r'^reporte/maquinistas/$', reporte_maquinistas_list_view, name='reporte_maquinistas_list_view'),
    url(r'^reporte/servicios/$', reporte_servicios_list_view, name='reporte_servicios_list_view'),
    url(r'^reporte/mantenciones/$', reporte_mantenciones_list_view, name='reporte_mantenciones_list_view'),
    url(r'^reporte/talleres/$', reporte_talleres_list_view, name='reporte_talleres_list_view'),
    url(r'^get_maquinas_compania/$', get_maquinas_compania, name='get_maquinas_compania'),

    #UTIL
    url(r'^get_all_conductores/$', get_all_conductores, name='get_all_conductores'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'Administración Control de flota'
