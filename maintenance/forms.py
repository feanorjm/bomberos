from django import forms

from maintenance.models import *

class BitacoraForm(forms.ModelForm):
    class Meta:
        model = Bitacora
        fields = ['compania','maquina', 'conductor', 'direccion', 'fecha',
                  'hora_salida','hora_llegada','clave','kilometraje_salida',
                  'kilometraje_llegada','hodometro_salida','hodometro_llegada',
                  'ho_bomba_salida','ho_bomba_regreso','observciones',]
        widgets = {
            'compania': forms.Select(attrs={'class': 'form-control'}),
            #'maquina': forms.Select(attrs={'class': 'form-control'}),
            #'conductor': forms.Select(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'id': 'fecha', 'class': 'date-picker form-control'}),
            'hora_salida': forms.TimeInput(attrs={'id':'hora_sal','type':'time', 'class': 'form-control'}),
            'hora_llegada': forms.TimeInput(attrs={'id':'hora_lle', 'type':'time', 'class': 'form-control'}),
            'clave': forms.Select(attrs={'class': 'form-control'}),
            'kilometraje_salida': forms.NumberInput(attrs={'class': 'form-control'}),
            'kilometraje_llegada': forms.NumberInput( attrs={'class': 'form-control'}),
            'hodometro_salida': forms.NumberInput(attrs={'class': 'form-control'}),
            'hodometro_llegada': forms.NumberInput(attrs={'class': 'form-control'}),
            'ho_bomba_salida': forms.NumberInput(attrs={'class': 'form-control'}),
            'ho_bomba_regreso': forms.NumberInput(attrs={'class': 'form-control'}),
            'observciones': forms.Textarea(attrs={'class': 'form-control', 'style': 'height: 90px;'}),

        }

class MantencionForm(forms.ModelForm):

    class Meta:
        model = Mantencion
        fields = ['fecha', 'compania', 'maquina', 'ki_salida', 'ki_regreso', 'ho_salida', 'ho_regreso', 'cod_man',
                  'observacion', 'num_factura', 'valor', 'taller', 'responsable']
        widgets = {
            'fecha': forms.DateInput(attrs={'id': 'fecha','class': 'form-control',}),
            'compania': forms.Select(attrs={'class': 'form-control'}),
            #'maquina': forms.Select(attrs={'class': 'form-control'}),
            'ki_salida': forms.NumberInput(attrs={'class': 'form-control'}),
            'ki_regreso': forms.NumberInput(attrs={'class': 'form-control'}),
            'ho_salida': forms.NumberInput(attrs={'class': 'form-control'}),
            'ho_regreso': forms.NumberInput(attrs={'class': 'form-control'}),
            #'tipo_mantencion': forms.Select(attrs={'class': 'form-control'}),
            'cod_man': forms.TextInput(attrs={'class': 'form-control'}),
            #'servicio': forms.Select(),
            'observacion': forms.Textarea(attrs={'class': 'form-control', 'style': 'height: 90px; width: 330px'}),
            'num_factura':forms.TextInput(attrs={'class': 'form-control','pattern': '[0-9]*'}),
            'valor':forms.TextInput(attrs={'class': 'form-control','pattern': '[0-9]*'}),
            'taller': forms.Select(attrs={'class': 'form-control'}),
            'responsable': forms.TextInput(attrs={'class': 'form-control'})
        }


class DetalleMantencionForm(forms.ModelForm):
    class Meta:
        model = DetalleMantencion
        fields = ['mantencion', 'division', 'subdivision', 'tipo_mantencion', 'servicio', 'des_detalle', 'hodometro_prox_man',]
        widgets = {
            'mantencion':forms.HiddenInput(),
            #'componente': forms.Select(attrs={'class': 'form-control'}),
            'division': forms.Select(attrs={'class': 'form-control'}),
            #'subdivision': forms.Select(attrs={'class': 'form-control'}),
            'tipo_mantencion': forms.Select(attrs={'class': 'form-control'}),
            #'servicio': forms.Select(attrs={'class': 'form-control'}),
            'des_detalle': forms.Textarea(attrs={'class': 'form-control', 'style': 'height: 90px;'}),
            'hodometro_prox_man': forms.NumberInput(attrs={'class': 'form-control'}),
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
    #conductor = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple,queryset=Conductor.objects.filter(compania__id = 1))
    class Meta:
        model = Maquina
        fields = {'nombre',
                  'clasificacion',
                  'compania',
                  'marca',
                  'modelo',
                  'ano',
                  'numero_motor',
                  'numero_chasis',
                  'bin',
                  'patente',
                  'conductor',
                  'kilometraje',
                  'hodometro',
                  'tiene_bomba',
                  'hodometro_bomba',
                  'venc_patente',
                  'costo_patente',
                  'soap_costo',
                  'venc_rev_tec',
                  'costo_rev_tec',
                  'costo_seg_auto',
                  'venc_seg_auto',
        }


        widgets = {
            'nombre':forms.TextInput(attrs={'class': 'form-control'}),
            'clasificacion': forms.Select(attrs={'class': 'form-control'}),
            'compania': forms.Select(attrs={'class': 'form-control'}),
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'ano': forms.Select(attrs={'class': 'form-control'}),
            'numero_motor': forms.TextInput(attrs={'class': 'form-control'}),
            'numero_chasis': forms.TextInput(attrs={'class': 'form-control'}),
            'bin': forms.TextInput(attrs={'class': 'form-control'}),
            'patente': forms.TextInput(attrs={'class': 'form-control'}),
            'conductor': forms.CheckboxSelectMultiple(),
            'kilometraje': forms.NumberInput(attrs={'class': 'form-control'}),
            'hodometro': forms.NumberInput(attrs={'class': 'form-control'}),
            'tiene_bomba': forms.Select(attrs={'class': 'form-control'}),
            'hodometro_bomba': forms.NumberInput(attrs={'class': 'form-control'}),
            'venc_patente': forms.DateInput(attrs={'class': 'form-control','placeholder':'yyyy-mm-dd'}),
            'costo_patente': forms.TextInput(attrs={'class': 'form-control', 'pattern': '[0-9]*','placeholder':'ej:30000'}),
            'soap_costo': forms.TextInput(attrs={'class': 'form-control', 'pattern': '[0-9]*','placeholder':'ej:30000'}),
            'venc_rev_tec': forms.DateInput(attrs={'class': 'form-control','placeholder':'yyyy-mm-dd'}),
            'costo_rev_tec': forms.TextInput(attrs={'class': 'form-control', 'pattern': '[0-9]*'}),
            'costo_seg_auto': forms.TextInput(attrs={'class': 'form-control', 'pattern': '[0-9]*','placeholder':'ej:30000'}),
            'venc_seg_auto': forms.DateInput(attrs={'class': 'form-control','placeholder':'yyyy-mm-dd'}),
        }

class ConductorForm(forms.ModelForm):
    class Meta:
        model = Conductor
        #use_required_attribute = False
        fields = ['compania','rut', 'nombre', 'ap_paterno','ap_materno', 'num_licencia', 'venc_lic','foto']
        widgets = {
            'compania': forms.Select(attrs={'class': 'form-control'}),
            'rut': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'ap_paterno': forms.TextInput(attrs={'class': 'form-control'}),
            'ap_materno': forms.TextInput(attrs={'class': 'form-control'}),
            'num_licencia': forms.TextInput(attrs={'class': 'form-control'}),
            'venc_lic': forms.DateInput(attrs={'id': 'fecha', 'class': 'form-control'}),
            'foto': forms.FileInput(attrs={'class': 'form-control'})
        }

class CombustibleForm(forms.ModelForm):
    class Meta:
        model = Carguios_combustible
        fields = ['compania','maquina','litros','servicentro','km_salida','km_regreso','hm_salida','hm_regreso',
                  'ho_bomba_salida','ho_bomba_regreso','valor','conductor','obac','fecha','tarjeta_tct']
        widgets = {
            'compania': forms.Select(attrs={'class': 'form-control'}),
            #'maquina': forms.Select(attrs={'class': 'form-control'}),
            'litros': forms.NumberInput(attrs={'class': 'form-control'}),
            'servicentro': forms.Select(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'id': 'fecha', 'class': 'date-picker form-control'}),
            'km_salida': forms.NumberInput(attrs={'class': 'form-control'}),
            'km_regreso': forms.NumberInput(attrs={'class': 'form-control'}),
            'hm_salida': forms.NumberInput(attrs={'class': 'form-control'}),
            'hm_regreso': forms.NumberInput(attrs={'class': 'form-control'}),
            'ho_bomba_salida': forms.NumberInput(attrs={'class': 'form-control'}),
            'ho_bomba_regreso': forms.NumberInput(attrs={'class': 'form-control'}),
            'valor': forms.TextInput(attrs={'class': 'form-control','pattern': '[0-9]*'}),
            #'conductor': forms.Select(attrs={'class': 'form-control'}),
            'obac': forms.TextInput(attrs={'class': 'form-control'}),
            'tarjeta_tct': forms.TextInput(attrs={'class': 'form-control', 'pattern': '[0-9]*'}),
        }

