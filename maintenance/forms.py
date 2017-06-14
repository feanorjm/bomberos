from django import forms

from maintenance.models import Bitacora,Mantencion,DetalleMantencion,RepuestoDetalleMantencion,Maquina,Conductor

class BitacoraForm(forms.ModelForm):
    class Meta:
        model = Bitacora
        fields = ['compania','maquina', 'conductor', 'cliente', 'direccion', 'fecha',
                  'hora_salida','hora_llegada','clave','kilometraje_salida',
                  'kilometraje_llegada','hodometro_salida','hodometro_llegada','observciones']
        widgets = {
            'compania': forms.Select(attrs={'class': 'form-control'}),
            'maquina': forms.Select(attrs={'class': 'form-control'}),
            'conductor': forms.Select(attrs={'class': 'form-control'}),
            'cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'id': 'fecha', 'class': 'date-picker form-control'}),
            'hora_salida': forms.TimeInput(attrs={'class': 'form-control'}),
            'hora_llegada': forms.TimeInput(attrs={'class': 'form-control'}),
            'clave': forms.TextInput(attrs={'class': 'form-control'}),
            'kilometraje_salida': forms.TextInput(attrs={'class': 'form-control', 'pattern': '[0-9]*'}),
            'kilometraje_llegada': forms.TextInput( attrs={'class': 'form-control', 'pattern': '[0-9]*'}),
            'hodometro_salida': forms.TextInput(attrs={'class': 'form-control', 'pattern': '[0-9]*'}),
            'hodometro_llegada': forms.TextInput(attrs={'class': 'form-control', 'pattern': '[0-9]*'}),
            'observciones': forms.Textarea(attrs={'class': 'form-control', 'style': 'height: 90px;'}),

        }

class MantencionForm(forms.ModelForm):
    class Meta:
        model = Mantencion
        fields = ['fecha', 'maquina', 'kilometraje', 'hodometro', 'tipo_mantencion', 'cod_man',
                  'servicio', 'observacion', 'num_factura', 'valor',
                  'taller', 'responsable']
        widgets = {
            'fecha': forms.DateInput(attrs={'id': 'fecha','class': 'form-control',}),
            'maquina': forms.Select(attrs={'class': 'form-control'}),
            'kilometraje': forms.TextInput(attrs={'class': 'form-control','pattern': '[0-9]*'}),
            'hodometro': forms.TextInput(attrs={'class': 'form-control','pattern': '[0-9]*'}),
            'tipo_mantencion': forms.Select(attrs={'class': 'form-control'}),
            'cod_man': forms.TextInput(attrs={'class': 'form-control'}),
            #'servicio': forms.Select(),
            'observacion': forms.Textarea(attrs={'class': 'form-control', 'style': 'height: 90px; width: 505px'}),
            'num_factura':forms.TextInput(attrs={'class': 'form-control','pattern': '[0-9]*'}),
            'valor':forms.TextInput(attrs={'class': 'form-control','pattern': '[0-9]*'}),
            'taller': forms.Select(attrs={'class': 'form-control'}),
            'responsable': forms.TextInput(attrs={'class': 'form-control'})
        }


class DetalleMantencionForm(forms.ModelForm):
    class Meta:
        model = DetalleMantencion
        fields = ['mantencion', 'componente', 'des_detalle', 'hodometro_prox_man',]
        widgets = {
            'mantencion':forms.HiddenInput(),
            'componente': forms.Select(attrs={'class': 'form-control'}),
            'des_detalle': forms.Textarea(attrs={'class': 'form-control', 'style': 'height: 90px; width: 410px'}),
            'hodometro_prox_man': forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingrese Hodometro', 'pattern': '[0-9]*'}),
        }

class RepuestoDetalleMantencionForm(forms.ModelForm):
    class Meta:
        model = RepuestoDetalleMantencion
        fields = ['mantencion','detalle_mantencion','repuesto',]
        widgets = {
            'mantencion': forms.HiddenInput(attrs={'id': 'id_mantencion_detalle'}),
            'detalle_mantencion': forms.HiddenInput(),
            'repuesto': forms.TextInput(attrs={'class': 'form-control'}),
        }

class MaquinaForm(forms.ModelForm):
    class Meta:
        model = Maquina
        fields = ['nombre','clasificacion', 'compania', 'marca','modelo','ano',
                  'numero_motor','numero_chasis','bin',
                  'patente', 'conductor', 'kilometraje','hodometro',]
        widgets = {
            'nombre':forms.TextInput(attrs={'class': 'form-control'}),
            'clasificacion': forms.Select(attrs={'class': 'form-control'}),
            'compania': forms.Select(attrs={'class': 'form-control'}),
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'ano': forms.Select(attrs={'class': 'form-control', 'pattern': '[0-9]*'}),
            'numero_motor': forms.TextInput(attrs={'class': 'form-control'}),
            'numero_chasis': forms.TextInput(attrs={'class': 'form-control'}),
            'bin': forms.TextInput(attrs={'class': 'form-control'}),
            'patente': forms.TextInput(attrs={'class': 'form-control'}),
            'conductor': forms.Select(attrs={'class': 'form-control'}),
            'kilometraje': forms.TextInput(attrs={'class': 'form-control', 'pattern': '[0-9]*'}),
            'hodometro': forms.TextInput(attrs={'class': 'form-control', 'pattern': '[0-9]*'}),
        }

class ConductorForm(forms.ModelForm):
    class Meta:
        model = Conductor
        #use_required_attribute = False
        fields = ['compania','rut', 'nombre', 'num_licencia', 'venc_lic','foto']
        widgets = {
            'compania': forms.Select(attrs={'class': 'form-control'}),
            'rut': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'num_licencia': forms.TextInput(attrs={'class': 'form-control'}),
            'venc_lic': forms.DateInput(attrs={'id': 'fecha', 'class': 'form-control'}),
            'foto': forms.FileInput(attrs={'class': 'form-control'})
        }

