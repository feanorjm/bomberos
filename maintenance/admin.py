from django.contrib import admin

from maintenance.models import UsuarioComp,Compania,Clasificacion_maquina,Maquina,Detalle_Maquina

class UsuarioCompAdmin(admin.ModelAdmin):
    list_display = ('user','tipo','compania')
    list_filter = ['user','tipo','compania']

class CompaniaAdmin(admin.ModelAdmin):
    list_display = ('nombre','numero')
    list_filter = ['nombre','numero']

class ClasificacionAdmin(admin.ModelAdmin):
    list_display = ('nombre','descripcion')
    list_filter = ['nombre','descripcion']

class MaquinaAdmin(admin.ModelAdmin):
    list_display = ('nombre','clasificacion','compania')
    list_filter = ['nombre','clasificacion','compania']

admin.site.register(UsuarioComp,UsuarioCompAdmin)
admin.site.register(Compania,CompaniaAdmin)
admin.site.register(Clasificacion_maquina,ClasificacionAdmin)
admin.site.register(Maquina,MaquinaAdmin)

'''admin.site.register(TblComuna,ComunaAdmin)
admin.site.register(TblProvincia,ProvinciaAdmin)
admin.site.register(TblRegion,RegionAdmin)
'''
