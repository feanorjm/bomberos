from django.conf.urls import url, include
from django.contrib import admin
from bomberos.views import login_view,logout_view
from maintenance.views import bitacora_create_view, bitacora_list,bitacora_detail

urlpatterns = [
    url(r'^chaining/', include('smart_selects.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', login_view,name='login_view'),
    url(r'^logout/$', logout_view, name='logout_view'),
    url(r'^bitacora/add/$', bitacora_create_view, name='bitacora_create_view'),
    url(r'^bitacora/$', bitacora_list, name='bitacora_list'),
    url(r'^bitacora/detalle/(?P<pk>\d+)$', bitacora_detail, name='bitacora_detail'),
]
