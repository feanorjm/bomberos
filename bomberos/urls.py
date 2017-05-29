from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^chaining/', include('smart_selects.urls')),
    url(r'^admin/', admin.site.urls),
]
