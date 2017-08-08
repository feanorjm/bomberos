from django.db import models
from smart_selects.db_fields import ChainedForeignKey, GroupedForeignKey, ChainedManyToManyField
from django.contrib.auth.models import User
from django.urls import reverse
import datetime
#from _overlapped import NULL


class Compania(models.Model):
    numero = models.IntegerField()
    nombre = models.CharField(max_length=45)
    direccion = models.CharField(max_length=45)

    def __str__(self):
        return str(self.nombre)

class Clasificacion_maquina(models.Model):
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=100,null=True, blank=True)

    def __str__(self):
        return str(self.nombre)

class Conductor(models.Model):
    compania = models.ForeignKey(Compania,null=True)
    rut = models.CharField(max_length=12, null=True,blank=True)
    nombre = models.CharField(max_length=45, null=True)
    ap_paterno = models.CharField(max_length=45, null=True)
    ap_materno = models.CharField(max_length=45, null=True)
    num_licencia = models.CharField(max_length=12, null=True,blank=True)
    venc_lic = models.DateField(null=True,blank=True)
    foto = models.FileField(upload_to='profile',null=True,blank=True)

    def __str__(self):
        nombre = self.nombre
        nombre = nombre.split(" ")
        return nombre[0] + " " + str(self.ap_paterno) + " " + str(self.ap_materno)

    def get_absolute_url(self):
        return reverse('conductor_detail', args=[str(self.id)])

year_dropdown = []
for y in range(1950, (datetime.datetime.now().year + 1)):
    year_dropdown.append((str(y), str(y)))

class Maquina(models.Model):
    nombre = models.CharField(max_length=45)
    clasificacion = models.ForeignKey(Clasificacion_maquina)
    compania = models.ForeignKey(Compania)
    marca = models.CharField(max_length=45,null=True, blank=True)
    modelo = models.CharField(max_length=45,null=True, blank=True)
    ano = models.CharField(max_length=5,choices=year_dropdown, default=datetime.datetime.now().year,null=True, blank=True)
    numero_motor = models.CharField(max_length=45,null=True, blank=True)
    numero_chasis = models.CharField(max_length=45,null=True, blank=True)
    bin = models.CharField(max_length=45,null=True, blank=True)
    patente = models.CharField(max_length=10,null=True, blank=True)
    conductor = models.ManyToManyField(Conductor, blank=True)
    #conductor = ChainedManyToManyField(Conductor, chained_field='compania', chained_model_field='compania', blank=True, horizontal=True)
    kilometraje = models.DecimalField(decimal_places=1,max_digits=10, null=True, blank=True)
    hodometro = models.DecimalField(decimal_places=1,max_digits=10, null=True, blank=True)
    tiene_bomba = models.BooleanField(default=False, choices=((True,"Si"),(False,"No")))
    hodometro_bomba = models.DecimalField(decimal_places=1,max_digits=10, null=True, blank=True)
    venc_patente = models.DateField(null=True, blank=True)  # vencimiento patente
    costo_patente = models.IntegerField(null=True, blank=True)  # costo patente
    soap_costo = models.IntegerField(null=True, blank=True)  # seguro obligatorio
    venc_rev_tec = models.DateField(null=True, blank=True)  # vencimiento revicion tecnica
    costo_rev_tec = models.IntegerField(null=True, blank=True)  # costo revision tecnica
    costo_seg_auto = models.IntegerField(null=True, blank=True)  # costo seguro automotriz
    venc_seg_auto = models.DateField(null=True, blank=True)
    prueba = models.DecimalField(decimal_places=1,max_digits=10, null=True, blank=True)

    def __str__(self):
        return str(self.nombre)

    def get_absolute_url(self):
        return reverse('maquina_detail', args=[str(self.id)])

# class Detalle_Maquina(models.Model):
#     maquina = models.ForeignKey(Maquina)
#     venc_patente = models.DateField()       #vencimiento patente
#     costo_patente = models.IntegerField()   #costo patente
#     soap_costo = models.IntegerField()      #seguro obligatorio
#     venc_rev_tec = models.DateField()       #vencimiento revicion tecnica
#     costo_rev_tec = models.IntegerField()   #costo revision tecnica
#     costo_seg_auto = models.IntegerField()  #costo seguro automotriz
#     venc_seg_auto = models.DateField(null=True)


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

    def get_tipo(self):
        return self.tipo

class Servicentro(models.Model):
    nombre = models.CharField(max_length=45)
    direccion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre + " - " + self.direccion

class Taller(models.Model):
    tipo = models.CharField(max_length=45)
    razon_social = models.CharField(max_length=45)
    rut = models.CharField(max_length=12, null=True, blank=True)
    telefono = models.IntegerField(null=True, blank=True)
    contacto = models.CharField(max_length=45, null=True, blank=True)
    tel_contacto = models.IntegerField(null=True, blank=True)
    direccion = models.CharField(max_length=60, null=True, blank=True)
    correo = models.EmailField(max_length=45, null=True, blank=True)

    def __str__(self):
        return str(self.razon_social)

class Componente(models.Model):
    nombre = models.CharField(max_length=45)
    descripcion = models.TextField(max_length=100)

    def __str__(self):
        return str(self.nombre)



class Division(models.Model):
    nombre = models.CharField(max_length=45)

    def __str__(self):
        return str(self.nombre)

class TipoMantencion(models.Model):
    nombre = models.CharField(max_length=45)
    descripcion = models.TextField(max_length=100)

    def __str__(self):
        return str(self.nombre)

class Subdivision(models.Model):
    division = models.ForeignKey(Division)
    nombre = models.CharField(max_length=45)

    def __str__(self):
        return str(self.nombre)



class ServicioMantencion(models.Model):
    division = models.ForeignKey(Division, null=True)
    subdivision = ChainedForeignKey(Subdivision, chained_field="division", chained_model_field="division",
                                related_name='%(class)s_requests_created', null=True)
    #tipo_mantencion = models.ForeignKey(TipoMantencion)
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=75, null=True, blank=True)

    def __str__(self):
        return str(self.nombre)




class Clave(models.Model):
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return str(self.nombre) + ' - ' + str(self.descripcion)

class Bitacora(models.Model):
    compania = models.ForeignKey(Compania)
    maquina = ChainedForeignKey(Maquina,chained_field="compania",chained_model_field="compania", related_name='%(class)s_requests_created')
    conductor = ChainedForeignKey(Conductor,chained_field="maquina",chained_model_field="maquina" , null=True)
    direccion = models.CharField(max_length=100,null=True)
    fecha = models.DateField(auto_now=False, auto_now_add=False,null=True)
    hora_salida = models.TimeField(null=True)
    hora_llegada = models.TimeField(null=True)
    clave = models.ForeignKey(Clave, null=True)
    kilometraje_salida = models.DecimalField(decimal_places=1,max_digits=10, null=True)
    kilometraje_llegada = models.DecimalField(decimal_places=1,max_digits=10, null=True)
    hodometro_salida = models.DecimalField(decimal_places=1,max_digits=10, null=True)
    hodometro_llegada = models.DecimalField(decimal_places=1,max_digits=10, null=True)
    ho_bomba_salida = models.DecimalField(decimal_places=1, max_digits=10, null=True, blank=True)
    ho_bomba_regreso = models.DecimalField(decimal_places=1, max_digits=10, null=True, blank=True)
    observciones = models.TextField(max_length=300,null=True)

    def __str__(self):
        return str(self.compania) +' - '+ str(self.maquina)+' - '+ str(self.fecha)+' - '+ str(self.clave)

    def get_absolute_url(self):
        return reverse('bitacora_detail', args=[str(self.id)])

class Mantencion(models.Model):
    fecha = models.DateField()
    compania = models.ForeignKey(Compania,null=True)
    maquina = ChainedForeignKey(Maquina, chained_field="compania", chained_model_field="compania",
                                related_name='%(class)s_requests_created')
    ki_salida = models.DecimalField(decimal_places=1,max_digits=10, null=True)
    ho_salida = models.DecimalField(decimal_places=1,max_digits=10, null=True)
    ki_regreso = models.DecimalField(decimal_places=1,max_digits=10, null=True)
    ho_regreso = models.DecimalField(decimal_places=1,max_digits=10, null=True)
    ho_bomba_salida = models.DecimalField(decimal_places=1, max_digits=10, null=True, blank=True)
    ho_bomba_regreso = models.DecimalField(decimal_places=1, max_digits=10, null=True, blank=True)
    cod_man = models.CharField(max_length=45) #orden de trabajo
    observacion = models.TextField(max_length=200)
    num_factura = models.IntegerField(null=True, blank=True)
    valor = models.IntegerField(null=True, blank=True)
    taller = models.ForeignKey(Taller)
    responsable = ChainedForeignKey(Conductor, chained_field="maquina", chained_model_field="maquina", null=True,
                                  blank=True)
    servicio = models.ForeignKey(Bitacora, null=True, blank=True)

    def __str__(self):
        return str(self.maquina) +'-'+ str(self.cod_man)

    def get_absolute_url(self):
        return reverse('mantencion_detail', args=[str(self.id)])

class DetalleMantencion(models.Model):
    mantencion = models.ForeignKey(Mantencion)
    division = models.ForeignKey(Division, null=True)
    subdivision = ChainedForeignKey(Subdivision, chained_field="division", chained_model_field="division", null=True, related_name='%(class)s_requests_created')
    tipo_mantencion = models.ForeignKey(TipoMantencion, default=1, null=True)
    servicio = ChainedForeignKey(ServicioMantencion, chained_field="subdivision", chained_model_field="subdivision", null=True, related_name='%(class)s_requests_created')
    des_detalle = models.TextField(max_length=200, null=True, blank=True)
    hodometro_prox_man = models.DecimalField(decimal_places=1,max_digits=10, null=True, blank=True)

    def __str__(self):
        return str(self.servicio)


class RepuestoDetalleMantencion(models.Model):
    mantencion = models.ForeignKey(Mantencion)
    detalle_mantencion = ChainedForeignKey(DetalleMantencion,chained_field="mantencion",chained_model_field="mantencion")
    repuesto = models.CharField(max_length=45, null=True, blank=True)

    def __str__(self):
        return str(self.repuesto)



class Carguios_combustible(models.Model):
    compania = models.ForeignKey(Compania, null=True)
    maquina = ChainedForeignKey(Maquina, chained_field="compania", chained_model_field="compania",
                                related_name='%(class)s_requests_created')
    litros = models.DecimalField(decimal_places=1,max_digits=10, null=True)
    servicentro = models.ForeignKey(Servicentro)
    km_salida = models.DecimalField(decimal_places=1,max_digits=10, null=True)
    hm_salida = models.DecimalField(decimal_places=1,max_digits=10, null=True)
    km_regreso = models.DecimalField(decimal_places=1,max_digits=10, null=True)
    hm_regreso = models.DecimalField(decimal_places=1,max_digits=10, null=True)
    ho_bomba_salida = models.DecimalField(decimal_places=1, max_digits=10, null=True, blank=True)
    ho_bomba_regreso = models.DecimalField(decimal_places=1, max_digits=10, null=True, blank=True)
    valor = models.IntegerField()
    tarjeta_tct = models.IntegerField()
    conductor = ChainedForeignKey(Conductor, chained_field="maquina", chained_model_field="maquina", null=True,
                                  blank=True)
    obac = models.CharField(max_length=45, null=True, blank=True)
    fecha = models.DateField(null=True)
    servicio = models.ForeignKey(Bitacora,null=True,blank=True)

    def __str__(self):
        return str(self.maquina)

    def get_absolute_url(self):
        return reverse('combustible_detail', args=[str(self.id)])





