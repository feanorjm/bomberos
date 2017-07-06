from django.contrib import admin
from django import forms
from maintenance.models import *

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
    #filter_horizontal = ('conductor',)

    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        if db_field.name == 'conductor':
            kwargs['widget'] = forms.CheckboxSelectMultiple()
            kwargs['help_text'] = ''

        return db_field.formfield(**kwargs)

class ServicentroAdmin(admin.ModelAdmin):
    list_display = ('nombre','direccion')
    list_filter = ['nombre','direccion']

class ClaveAdmin(admin.ModelAdmin):
    list_display = ('nombre','descripcion')
    list_filter = ['nombre','descripcion']

class TallerAdmin(admin.ModelAdmin):
    list_display = ('razon_social','tipo','telefono')
    list_filter = ['razon_social','tipo','telefono']

class CarguioAdmin(admin.ModelAdmin):
    list_display = ('maquina','litros','servicentro','valor')
    list_filter = ['maquina',]

class TipoMantencionAdmin(admin.ModelAdmin):
    list_display = ('nombre','descripcion')
    list_filter = ['nombre',]

class ServicioMantencionAdmin(admin.ModelAdmin):
    list_display = ('nombre','tipo_mantencion','descripcion')
    list_filter = ['nombre','tipo_mantencion']

class MantencionAdmin(admin.ModelAdmin):
    list_display = ('fecha','maquina','tipo_mantencion','servicio')
    list_filter = ['fecha','maquina','tipo_mantencion','servicio']

class DetalleMantencionAdmin(admin.ModelAdmin):
    list_display = ('mantencion','componente','des_detalle','hodometro_prox_man')
    list_filter = ['mantencion','componente','hodometro_prox_man']

class RepuestoDetalleMantencionAdmin(admin.ModelAdmin):
    list_display = ('mantencion','detalle_mantencion','repuesto')
    list_filter = ['mantencion','detalle_mantencion','repuesto']

class BitacoraAdmin(admin.ModelAdmin):
    list_display = ('compania', 'maquina', 'conductor','clave','fecha','observciones')
    list_filter = ['compania', 'maquina']

class CambioNeumaticoAdmin(admin.ModelAdmin):
    list_display = ('compania', 'maquina', 'fecha', 'kilometraje','marca','modelo','proveedor')
    list_filter = ['compania', 'maquina', 'fecha']

class ComponenteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    list_filter = ['nombre', ]


admin.site.register(UsuarioComp,UsuarioCompAdmin)
admin.site.register(Compania,CompaniaAdmin)
admin.site.register(Clasificacion_maquina,ClasificacionAdmin)
admin.site.register(Conductor,ConductorAdmin)
admin.site.register(Maquina,MaquinaAdmin)
admin.site.register(Servicentro,ServicentroAdmin)
admin.site.register(Taller,TallerAdmin)
admin.site.register(Carguios_combustible,CarguioAdmin)
admin.site.register(TipoMantencion,TipoMantencionAdmin)
admin.site.register(ServicioMantencion,ServicioMantencionAdmin)
admin.site.register(Mantencion,MantencionAdmin)
admin.site.register(DetalleMantencion,DetalleMantencionAdmin)
admin.site.register(RepuestoDetalleMantencion,RepuestoDetalleMantencionAdmin)
admin.site.register(Bitacora,BitacoraAdmin)
admin.site.register(CambioNeumatico,CambioNeumaticoAdmin)
admin.site.register(Componente,ComponenteAdmin)
admin.site.register(Clave,ClaveAdmin)


