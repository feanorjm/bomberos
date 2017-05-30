from django.conf.urls import url, include
from django.contrib import admin
from bomberos.views import login_view,logout_view

urlpatterns = [
    url(r'^chaining/', include('smart_selects.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^login/', login_view,name='login_view'),
    url(r'^logout/', logout_view, name='logout_view'),
]
