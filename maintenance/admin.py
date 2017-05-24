from django.contrib import admin

from maintenance.models import (UsuarioComp,
                                Compania,
                                Clasificacion_maquina,
                                Conductor,
                                Maquina,
                                Detalle_Maquina,
                                Servicentro,
                                Taller)

class UsuarioCompAdmin(admin.ModelAdmin):
    list_display = ('user','tipo','compania')
    list_filter = ['tipo','compania']

class CompaniaAdmin(admin.ModelAdmin):
    list_display = ('nombre','numero')
    list_filter = ['nombre','numero']

class ClasificacionAdmin(admin.ModelAdmin):
    list_display = ('nombre','descripcion')
    list_filter = ['nombre','descripcion']

class ConductorAdmin(admin.ModelAdmin):
    list_display = ('nombre','rut')
    list_filter = ['nombre','rut']

class MaquinaAdmin(admin.ModelAdmin):
    list_display = ('nombre','clasificacion','compania')
    list_filter = ['nombre','clasificacion','compania']

class ServicentroAdmin(admin.ModelAdmin):
    list_display = ('nombre','direccion')
    list_filter = ['nombre','direccion']

class TallerAdmin(admin.ModelAdmin):
    list_display = ('razon_social','tipo','telefono')
    list_filter = ['nombre','tipo','telefono']

admin.site.register(UsuarioComp,UsuarioCompAdmin)
admin.site.register(Compania,CompaniaAdmin)
admin.site.register(Clasificacion_maquina,ClasificacionAdmin)
admin.site.register(Conductor,ConductorAdmin)
admin.site.register(Maquina,MaquinaAdmin)
admin.site.register(Servicentro,ServicentroAdmin)

'''admin.site.register(TblComuna,ComunaAdmin)
admin.site.register(TblProvincia,ProvinciaAdmin)
admin.site.register(TblRegion,RegionAdmin)
'''
