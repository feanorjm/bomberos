from django import forms

from maintenance.models import Bitacora

class BitacoraForm(forms.ModelForm):
    class Meta:
        model = Bitacora
        fields = ['compania','maquina', 'conductor', 'cliente', 'fecha',
                  'hora_salida','hora_llegada','clave','kilometraje_salida',
                  'kilometraje_llegada','hodometro_salida','hodometro_llegada','observciones']
        widgets = {
            'compania': forms.Select(attrs={'class': 'form-control col-md-7 col-xs-12"'}),
            'maquina': forms.Select(attrs={'class': 'form-control col-md-7 col-xs-12"'}),
            'conductor': forms.Select(attrs={'class': 'form-control col-md-7 col-xs-12"'}),
            'cliente': forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12'}),
            'fecha': forms.DateInput(attrs={'id': 'fecha', 'class': 'date-picker form-control col-md-7 col-xs-12"'}),
            'hora_salida': forms.TimeInput(attrs={'class': 'form-control col-md-7 col-xs-12"'}),
            'hora_llegada': forms.TimeInput(attrs={'class': 'form-control col-md-7 col-xs-12"'}),
            'clave': forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12'}),
            'kilometraje_salida': forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12', 'pattern': '[0-9]*'}),
            'kilometraje_llegada': forms.TextInput( attrs={'class': 'form-control col-md-7 col-xs-12', 'pattern': '[0-9]*'}),
            'hodometro_salida': forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12', 'pattern': '[0-9]*'}),
            'hodometro_llegada': forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12', 'pattern': '[0-9]*'}),
            'observciones': forms.Textarea(attrs={'class': 'form-control col-md-7 col-xs-12"', 'style': 'height: 90px;'}),

        }