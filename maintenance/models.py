from django.db import models
from smart_selects.db_fields import ChainedForeignKey
from django.contrib.auth.models import User
from django.urls import reverse
import datetime


class Compania(models.Model):
    numero = models.IntegerField()
    nombre = models.CharField(max_length=45)
    direccion = models.CharField(max_length=45)

    def __str__(self):
        return self.nombre

class Clasificacion_maquina(models.Model):
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=100,null=True, blank=True)

    def __str__(self):
        return self.nombre

class Conductor(models.Model):
    compania = models.ForeignKey(Compania,null=True)
    rut = models.CharField(max_length=12)
    nombre = models.CharField(max_length=45)
    num_licencia = models.CharField(max_length=12)
    venc_lic = models.DateField()
    foto = models.FileField(upload_to='profile',null=True,blank=True)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('conductor_detail', args=[str(self.id)])

year_dropdown = []
for y in range(1950, (datetime.datetime.now().year + 1)):
    year_dropdown.append((y, y))

class Maquina(models.Model):
    nombre = models.CharField(max_length=45)
    clasificacion = models.ForeignKey(Clasificacion_maquina)
    compania = models.ForeignKey(Compania)
    marca = models.CharField(max_length=45,null=True)
    modelo = models.CharField(max_length=45,null=True)
    ano = models.IntegerField(choices=year_dropdown, default=datetime.datetime.now().year)
    numero_motor = models.CharField(max_length=45)
    numero_chasis = models.CharField(max_length=45)
    bin = models.CharField(max_length=45)
    patente = models.CharField(max_length=10)
    conductor = models.ForeignKey(Conductor ,null=True, blank=True)
    kilometraje = models.IntegerField(null=True, blank=True)
    hodometro = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('maquina_detail', args=[str(self.id)])

class Detalle_Maquina(models.Model):
    maquina = models.ForeignKey(Maquina)
    venc_patente = models.DateField()       #vencimiento patente
    costo_patente = models.IntegerField()   #costo patente
    soap_costo = models.IntegerField()      #seguro obligatorio
    venc_rev_tec = models.DateField()       #vencimiento revicion tecnica
    costo_rev_tec = models.IntegerField()   #costo revision tecnica
    costo_seg_auto = models.IntegerField()  #costo seguro automotriz
    venc_seg_auto = models.DateField(null=True)


TIPO_USER_CHOICES = (
    ('0', 'Teniente de máquina'),
    ('1', 'OBAC'),
    ('2', 'Inspector general de máquina'),
    ('3', 'Comandante')
)

class UsuarioComp(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=1, choices=TIPO_USER_CHOICES)
    compania = models.ForeignKey(Compania, null=True)

    def __str__(self):
        return str(self.user)

class Servicentro(models.Model):
    nombre = models.CharField(max_length=45)
    direccion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Taller(models.Model):
    tipo = models.CharField(max_length=45)
    razon_social = models.CharField(max_length=45)
    rut = models.CharField(max_length=12)
    telefono = models.IntegerField()
    contacto = models.CharField(max_length=45)
    tel_contacto = models.IntegerField()
    direccion = models.CharField(max_length=60)
    correo = models.EmailField(max_length=45)

    def __str__(self):
        return self.razon_social

class Carguios_combustible(models.Model):
    maquina = models.ForeignKey(Maquina)
    litros = models.IntegerField()
    servicentro = models.ForeignKey(Servicentro)
    kilometraje = models.IntegerField()
    hodometro = models.IntegerField()
    valor = models.IntegerField()
    conductor = models.ForeignKey(Conductor)
    obac = models.ForeignKey(User)

    def __str__(self):
        return str(self.maquina)

class TipoMantencion(models.Model):
    nombre = models.CharField(max_length=45)
    descripcion = models.TextField(max_length=100)

    def __str__(self):
        return self.nombre

class ServicioMantencion(models.Model):
    tipo_mantencion = models.ForeignKey(TipoMantencion)
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=75, null=True, blank=True)

    def __str__(self):
        return self.nombre

class Mantencion(models.Model):
    fecha = models.DateField()
    maquina = models.ForeignKey(Maquina)
    kilometraje = models.IntegerField()
    hodometro = models.IntegerField()
    tipo_mantencion = models.ForeignKey(TipoMantencion, default=1)
    cod_man = models.CharField(max_length=45)
    servicio = ChainedForeignKey(ServicioMantencion,chained_field="tipo_mantencion",chained_model_field="tipo_mantencion")
    observacion = models.TextField(max_length=200)
    num_factura = models.IntegerField()
    valor = models.IntegerField()
    taller = models.ForeignKey(Taller)
    responsable = models.CharField(max_length=45)

    def __str__(self):
        return str(self.maquina) +'-'+ str(self.tipo_mantencion)+'-'+ str(self.servicio)

    def get_absolute_url(self):
        return reverse('mantencion_detail', args=[str(self.id)])

class DetalleMantencion(models.Model):
    mantencion = models.ForeignKey(Mantencion)
    componente = models.CharField(max_length=50, null=True)
    des_detalle = models.TextField(max_length=150)
    hodometro_prox_man = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.componente


class RepuestoDetalleMantencion(models.Model):
    mantencion = models.ForeignKey(Mantencion)
    detalle_mantencion = ChainedForeignKey(DetalleMantencion,chained_field="mantencion",chained_model_field="mantencion")
    repuesto = models.CharField(max_length=45)

    def __str__(self):
        return self.repuesto

class Bitacora(models.Model):
    compania = models.ForeignKey(Compania)
    maquina = ChainedForeignKey(Maquina,chained_field="compania",chained_model_field="compania")
    conductor = ChainedForeignKey(Conductor,chained_field="compania",chained_model_field="compania",default=1)
    cliente = models.CharField(max_length=45,null=True)
    direccion = models.CharField(max_length=100,null=True)
    fecha = models.DateField(auto_now=False, auto_now_add=False,null=True)
    hora_salida = models.TimeField(null=True)
    hora_llegada = models.TimeField(null=True)
    clave = models.CharField(max_length=45,null=True)
    kilometraje_salida = models.IntegerField(null=True)
    kilometraje_llegada = models.IntegerField(null=True)
    hodometro_salida = models.IntegerField(null=True)
    hodometro_llegada = models.IntegerField(null=True)
    observciones = models.TextField(max_length=300,null=True)

    def __str__(self):
        return str(self.compania) +' - '+ str(self.maquina)+' - '+ str(self.fecha)+' - '+ str(self.clave)

    def get_absolute_url(self):
        return reverse('bitacora_detail', args=[str(self.id)])

class CambioNeumatico(models.Model):
    compania = models.ForeignKey(Compania)
    maquina = ChainedForeignKey(Maquina,chained_field="compania",chained_model_field="compania")
    fecha = models.DateField()
    kilometraje = models.IntegerField()
    hodometro = models.IntegerField()
    marca = models.CharField(max_length=45)
    modelo = models.CharField(max_length=45)
    medidas = models.CharField(max_length=45)
    proveedor = models.ForeignKey(Taller)
    valor = models.IntegerField()
    responsable = models.CharField(max_length=45)

    def __str__(self):
        return str(self.compania) +' - '+ str(self.maquina)+' - '+ str(self.fecha)

    def get_absolute_url(self):
        return "/cambioneumatico/%i/" % self.id




