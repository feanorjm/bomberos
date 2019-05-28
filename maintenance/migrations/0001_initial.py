# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-23 21:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bitacora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=100, null=True)),
                ('fecha', models.DateField(null=True)),
                ('hora_salida', models.TimeField(null=True)),
                ('hora_llegada', models.TimeField(null=True)),
                ('kilometraje_salida', models.DecimalField(decimal_places=1, max_digits=10, null=True)),
                ('kilometraje_llegada', models.DecimalField(decimal_places=1, max_digits=10, null=True)),
                ('hodometro_salida', models.DecimalField(decimal_places=1, max_digits=10, null=True)),
                ('hodometro_llegada', models.DecimalField(decimal_places=1, max_digits=10, null=True)),
                ('ho_bomba_salida', models.DecimalField(blank=True, decimal_places=1, max_digits=10, null=True)),
                ('ho_bomba_regreso', models.DecimalField(blank=True, decimal_places=1, max_digits=10, null=True)),
                ('observciones', models.TextField(max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Carguios_combustible',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('litros', models.DecimalField(decimal_places=1, max_digits=10, null=True)),
                ('km_salida', models.DecimalField(decimal_places=1, max_digits=10, null=True)),
                ('hm_salida', models.DecimalField(decimal_places=1, max_digits=10, null=True)),
                ('km_regreso', models.DecimalField(decimal_places=1, max_digits=10, null=True)),
                ('hm_regreso', models.DecimalField(decimal_places=1, max_digits=10, null=True)),
                ('ho_bomba_salida', models.DecimalField(blank=True, decimal_places=1, max_digits=10, null=True)),
                ('ho_bomba_regreso', models.DecimalField(blank=True, decimal_places=1, max_digits=10, null=True)),
                ('hora_salida', models.TimeField(null=True)),
                ('hora_llegada', models.TimeField(null=True)),
                ('valor', models.IntegerField()),
                ('tarjeta_tct', models.IntegerField()),
                ('obac', models.CharField(blank=True, max_length=45, null=True)),
                ('fecha', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Clasificacion_maquina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('descripcion', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Clave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Compania',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('nombre', models.CharField(max_length=45)),
                ('direccion', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Componente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('descripcion', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Conductor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(blank=True, max_length=12, null=True)),
                ('nombre', models.CharField(max_length=45, null=True)),
                ('ap_paterno', models.CharField(max_length=45, null=True)),
                ('ap_materno', models.CharField(max_length=45, null=True)),
                ('num_licencia', models.CharField(blank=True, max_length=12, null=True)),
                ('venc_lic', models.DateField(blank=True, null=True)),
                ('observaciones_cond', models.TextField(blank=True, default='Ninguna', max_length=1000, null=True)),
                ('foto', models.FileField(blank=True, null=True, upload_to='profile')),
                ('compania', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='maintenance.Compania')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleMantencion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('des_detalle', models.TextField(blank=True, max_length=200, null=True)),
                ('hodometro_prox_man', models.DecimalField(blank=True, decimal_places=1, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Mantencion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('ki_salida', models.DecimalField(decimal_places=1, max_digits=10, null=True)),
                ('ho_salida', models.DecimalField(decimal_places=1, max_digits=10, null=True)),
                ('ki_regreso', models.DecimalField(decimal_places=1, max_digits=10, null=True)),
                ('ho_regreso', models.DecimalField(decimal_places=1, max_digits=10, null=True)),
                ('ho_bomba_salida', models.DecimalField(blank=True, decimal_places=1, max_digits=10, null=True)),
                ('ho_bomba_regreso', models.DecimalField(blank=True, decimal_places=1, max_digits=10, null=True)),
                ('hora_salida', models.TimeField(null=True)),
                ('hora_llegada', models.TimeField(null=True)),
                ('cod_man', models.CharField(max_length=45)),
                ('observacion', models.TextField(max_length=200)),
                ('num_factura', models.IntegerField(blank=True, default=0)),
                ('valor', models.IntegerField(blank=True, default=0)),
                ('compania', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='maintenance.Compania')),
            ],
        ),
        migrations.CreateModel(
            name='Maquina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('marca', models.CharField(blank=True, max_length=45, null=True)),
                ('modelo', models.CharField(blank=True, max_length=45, null=True)),
                ('ano', models.CharField(blank=True, choices=[('1950', '1950'), ('1951', '1951'), ('1952', '1952'), ('1953', '1953'), ('1954', '1954'), ('1955', '1955'), ('1956', '1956'), ('1957', '1957'), ('1958', '1958'), ('1959', '1959'), ('1960', '1960'), ('1961', '1961'), ('1962', '1962'), ('1963', '1963'), ('1964', '1964'), ('1965', '1965'), ('1966', '1966'), ('1967', '1967'), ('1968', '1968'), ('1969', '1969'), ('1970', '1970'), ('1971', '1971'), ('1972', '1972'), ('1973', '1973'), ('1974', '1974'), ('1975', '1975'), ('1976', '1976'), ('1977', '1977'), ('1978', '1978'), ('1979', '1979'), ('1980', '1980'), ('1981', '1981'), ('1982', '1982'), ('1983', '1983'), ('1984', '1984'), ('1985', '1985'), ('1986', '1986'), ('1987', '1987'), ('1988', '1988'), ('1989', '1989'), ('1990', '1990'), ('1991', '1991'), ('1992', '1992'), ('1993', '1993'), ('1994', '1994'), ('1995', '1995'), ('1996', '1996'), ('1997', '1997'), ('1998', '1998'), ('1999', '1999'), ('2000', '2000'), ('2001', '2001'), ('2002', '2002'), ('2003', '2003'), ('2004', '2004'), ('2005', '2005'), ('2006', '2006'), ('2007', '2007'), ('2008', '2008'), ('2009', '2009'), ('2010', '2010'), ('2011', '2011'), ('2012', '2012'), ('2013', '2013'), ('2014', '2014'), ('2015', '2015'), ('2016', '2016'), ('2017', '2017'), ('2018', '2018'), ('2019', '2019')], default=2019, max_length=5, null=True)),
                ('numero_motor', models.CharField(blank=True, max_length=45, null=True)),
                ('numero_chasis', models.CharField(blank=True, max_length=45, null=True)),
                ('bin', models.CharField(blank=True, max_length=45, null=True)),
                ('patente', models.CharField(blank=True, max_length=10, null=True)),
                ('kilometraje', models.DecimalField(blank=True, decimal_places=1, max_digits=10, null=True)),
                ('hodometro', models.DecimalField(blank=True, decimal_places=1, max_digits=10, null=True)),
                ('tiene_bomba', models.BooleanField(choices=[(True, 'Si'), (False, 'No')], default=False)),
                ('hodometro_bomba', models.DecimalField(blank=True, decimal_places=1, max_digits=10, null=True)),
                ('venc_patente', models.DateField(blank=True, null=True)),
                ('costo_patente', models.IntegerField(blank=True, null=True)),
                ('soap_costo', models.IntegerField(blank=True, null=True)),
                ('venc_rev_tec', models.DateField(blank=True, null=True)),
                ('costo_rev_tec', models.IntegerField(blank=True, null=True)),
                ('costo_seg_auto', models.IntegerField(blank=True, null=True)),
                ('venc_seg_auto', models.DateField(blank=True, null=True)),
                ('prueba', models.DecimalField(blank=True, decimal_places=1, max_digits=10, null=True)),
                ('procedencia_maquina', models.CharField(choices=[('1', 'AMERICANO'), ('2', 'EUROPEO')], default=1, max_length=1)),
                ('clasificacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maintenance.Clasificacion_maquina')),
                ('compania', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maintenance.Compania')),
                ('conductor', models.ManyToManyField(blank=True, to='maintenance.Conductor')),
            ],
        ),
        migrations.CreateModel(
            name='RepuestoDetalleMantencion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repuesto', models.CharField(blank=True, max_length=45, null=True)),
                ('detalle_mantencion', smart_selects.db_fields.ChainedForeignKey(chained_field='mantencion', chained_model_field='mantencion', on_delete=django.db.models.deletion.CASCADE, to='maintenance.DetalleMantencion')),
                ('mantencion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maintenance.Mantencion')),
            ],
        ),
        migrations.CreateModel(
            name='Servicentro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('direccion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ServicioMantencion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('descripcion', models.CharField(blank=True, max_length=75, null=True)),
                ('division', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='maintenance.Division')),
            ],
        ),
        migrations.CreateModel(
            name='Subdivision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maintenance.Division')),
            ],
        ),
        migrations.CreateModel(
            name='Taller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=45)),
                ('razon_social', models.CharField(max_length=45)),
                ('rut', models.CharField(blank=True, max_length=12, null=True)),
                ('telefono', models.IntegerField(blank=True, null=True)),
                ('contacto', models.CharField(blank=True, max_length=45, null=True)),
                ('tel_contacto', models.IntegerField(blank=True, null=True)),
                ('direccion', models.CharField(blank=True, max_length=60, null=True)),
                ('correo', models.EmailField(blank=True, max_length=45, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TipoMantencion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('descripcion', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UsuarioComp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('0', 'Teniente de máquina'), ('1', 'OBAC'), ('2', 'Inspector general de máquina'), ('3', 'Comandante')], max_length=1)),
                ('compania', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='maintenance.Compania')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='serviciomantencion',
            name='subdivision',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='division', chained_model_field='division', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='serviciomantencion_requests_created', to='maintenance.Subdivision'),
        ),
        migrations.AddField(
            model_name='mantencion',
            name='maquina',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='compania', chained_model_field='compania', on_delete=django.db.models.deletion.CASCADE, related_name='mantencion_requests_created', to='maintenance.Maquina'),
        ),
        migrations.AddField(
            model_name='mantencion',
            name='responsable',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='maquina', chained_model_field='maquina', null=True, on_delete=django.db.models.deletion.CASCADE, to='maintenance.Conductor'),
        ),
        migrations.AddField(
            model_name='mantencion',
            name='servicio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='maintenance.Bitacora'),
        ),
        migrations.AddField(
            model_name='mantencion',
            name='taller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maintenance.Taller'),
        ),
        migrations.AddField(
            model_name='detallemantencion',
            name='division',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='maintenance.Division'),
        ),
        migrations.AddField(
            model_name='detallemantencion',
            name='mantencion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maintenance.Mantencion'),
        ),
        migrations.AddField(
            model_name='detallemantencion',
            name='servicio',
            field=smart_selects.db_fields.ChainedForeignKey(blank=True, chained_field='subdivision', chained_model_field='subdivision', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='detallemantencion_requests_created', to='maintenance.ServicioMantencion'),
        ),
        migrations.AddField(
            model_name='detallemantencion',
            name='subdivision',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='division', chained_model_field='division', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='detallemantencion_requests_created', to='maintenance.Subdivision'),
        ),
        migrations.AddField(
            model_name='detallemantencion',
            name='tipo_mantencion',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='maintenance.TipoMantencion'),
        ),
        migrations.AddField(
            model_name='carguios_combustible',
            name='compania',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='maintenance.Compania'),
        ),
        migrations.AddField(
            model_name='carguios_combustible',
            name='conductor',
            field=smart_selects.db_fields.ChainedForeignKey(blank=True, chained_field='maquina', chained_model_field='maquina', null=True, on_delete=django.db.models.deletion.CASCADE, to='maintenance.Conductor'),
        ),
        migrations.AddField(
            model_name='carguios_combustible',
            name='maquina',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='compania', chained_model_field='compania', on_delete=django.db.models.deletion.CASCADE, related_name='carguios_combustible_requests_created', to='maintenance.Maquina'),
        ),
        migrations.AddField(
            model_name='carguios_combustible',
            name='servicentro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maintenance.Servicentro'),
        ),
        migrations.AddField(
            model_name='carguios_combustible',
            name='servicio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='maintenance.Bitacora'),
        ),
        migrations.AddField(
            model_name='bitacora',
            name='clave',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='maintenance.Clave'),
        ),
        migrations.AddField(
            model_name='bitacora',
            name='compania',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maintenance.Compania'),
        ),
        migrations.AddField(
            model_name='bitacora',
            name='conductor',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='maquina', chained_model_field='maquina', null=True, on_delete=django.db.models.deletion.CASCADE, to='maintenance.Conductor'),
        ),
        migrations.AddField(
            model_name='bitacora',
            name='maquina',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='compania', chained_model_field='compania', on_delete=django.db.models.deletion.CASCADE, related_name='bitacora_requests_created', to='maintenance.Maquina'),
        ),
    ]
