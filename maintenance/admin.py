from django.contrib import admin
from django import forms
from maintenance.models import *
from django.contrib import messages

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
    list_display = ('nombre','ap_materno','ap_materno', 'compania')
    list_filter = ['compania',]

class MaquinaAdmin(admin.ModelAdmin):
    list_display = ('nombre','clasificacion','compania','tiene_bomba')
    list_filter = ['clasificacion','compania','tiene_bomba']
    filter_horizontal = ('conductor',)

    # def formfield_for_manytomany(self, db_field, request=None, **kwargs):
    #     if db_field.name == 'conductor':
    #         kwargs['widget'] = forms.CheckboxSelectMultiple()
    #         kwargs['help_text'] = ''
    #
    #     return db_field.formfield(**kwargs)

class ServicentroAdmin(admin.ModelAdmin):
    list_display = ('nombre','direccion')
    list_filter = ['nombre','direccion']

class ClaveAdmin(admin.ModelAdmin):
    list_display = ('nombre','descripcion','habilitado')
    list_filter = ['nombre','descripcion','habilitado']

    def delete_model(self, request, obj):
        if obj.nombre == '6--14':
            messages.add_message(request, messages.WARNING, 'Esta clave no se puede eliminar')
        else:
            obj.delete()
        return



class TallerAdmin(admin.ModelAdmin):
    list_display = ('razon_social','tipo','telefono')
    list_filter = ['razon_social','tipo','telefono']

class CarguioAdmin(admin.ModelAdmin):
    list_display = ('id','compania','servicio_id','maquina','litros','servicentro','valor')
    list_filter = ['compania','maquina',]

class TipoMantencionAdmin(admin.ModelAdmin):
    list_display = ('nombre','descripcion')
    list_filter = ['nombre',]

class ServicioMantencionAdmin(admin.ModelAdmin):
    list_display = ('nombre','division','subdivision','descripcion')
    list_filter = ['nombre','division','subdivision',]

class MantencionAdmin(admin.ModelAdmin):
    list_display = ('fecha','maquina',)
    list_filter = ['fecha','maquina',]

class DetalleMantencionAdmin(admin.ModelAdmin):
    list_display = ('mantencion','des_detalle','hodometro_prox_man')
    list_filter = ['mantencion','hodometro_prox_man']

class RepuestoDetalleMantencionAdmin(admin.ModelAdmin):
    list_display = ('mantencion','detalle_mantencion','repuesto')
    list_filter = ['mantencion','detalle_mantencion','repuesto']

class BitacoraAdmin(admin.ModelAdmin):
    list_display = ('id','compania', 'maquina', 'conductor','clave','fecha','observciones')
    list_filter = ['compania', 'maquina']

class ComponenteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    list_filter = ['nombre', ]

class DivisionAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    list_filter = ['nombre', ]

class SubdivisionAdmin(admin.ModelAdmin):
    list_display = ('nombre','division')
    list_filter = ['nombre','division' ]


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
admin.site.register(Componente,ComponenteAdmin)
admin.site.register(Clave,ClaveAdmin)
admin.site.register(Division,DivisionAdmin)
admin.site.register(Subdivision,SubdivisionAdmin)


