from django.db import models
from smart_selects.db_fields import ChainedForeignKey
from django.contrib.auth.models import User


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
    rut = models.CharField(max_length=12)
    nombre = models.CharField(max_length=45)
    num_licencia = models.CharField(max_length=12)
    venc_lic = models.DateField()

    def __str__(self):
        return self.nombre

class Maquina(models.Model):
    nombre = models.CharField(max_length=45)
    clasificacion = models.ForeignKey(Clasificacion_maquina)
    compania = models.ForeignKey(Compania)
    numero_motor = models.CharField(max_length=45)
    numero_chasis = models.CharField(max_length=45)
    bin = models.CharField(max_length=45)
    patente = models.CharField(max_length=10)
    conductor = models.ForeignKey(Conductor ,null=True, blank=True)

    def __str__(self):
        return self.nombre

class Detalle_Maquina(models.Model):
    maquina = models.ForeignKey(Maquina)
    venc_patente = models.DateField()       #vencimiento patente
    costo_patente = models.IntegerField()   #costo patente
    soap_costo = models.IntegerField()      #seguro obligatorio
    venc_rev_tec = models.DateField()       #vencimiento revicion tecnica
    costo_rev_tec = models.IntegerField()   #costo revision tecnica
    costo_seg_auto = models.IntegerField()  #costo seguro automotriz


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
        return self.first_name

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






