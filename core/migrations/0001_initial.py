# Generated by Django 2.1.2 on 2019-06-28 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estudio',
            fields=[
                ('id_estudio', models.AutoField(primary_key=True, serialize=False, verbose_name='Estudio')),
                ('fechaAcutal', models.DateTimeField(auto_now_add=True, verbose_name='Fecha Actual')),
                ('medico', models.CharField(max_length=50, verbose_name='Medico')),
                ('peso', models.FloatField(verbose_name='Peso')),
                ('talla', models.FloatField(verbose_name='Talla')),
                ('indicacion', models.CharField(max_length=50, verbose_name='Indicacion')),
                ('decubito', models.CharField(max_length=50, verbose_name='Decubito')),
                ('perimetroAbdominal', models.IntegerField(verbose_name='Perimetro Abdominal')),
                ('urgencia', models.BooleanField(default=False, verbose_name='Urgente')),
                ('edad', models.IntegerField(verbose_name='Edad')),
                ('imc', models.IntegerField(verbose_name='Imc')),
                ('supCorporal', models.FloatField(verbose_name='Superficie corporal')),
                ('calidadTecnica', models.IntegerField(verbose_name='Calidad tecnica')),
                ('observaciones', models.TextField(verbose_name='Observaciones')),
            ],
        ),
        migrations.CreateModel(
            name='InstitucionMedica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreInstitucion', models.CharField(max_length=60, verbose_name='Nombre de institucion')),
                ('calle', models.CharField(max_length=60, verbose_name='Calle')),
                ('barrio', models.CharField(max_length=60, verbose_name='Barrio')),
                ('numeracion', models.IntegerField(verbose_name='Numeracion')),
                ('pais', models.CharField(max_length=60, verbose_name='Pais')),
                ('ciudad', models.CharField(max_length=60, verbose_name='Ciudad')),
                ('provinciaEstado', models.CharField(max_length=60, verbose_name='Provincia')),
                ('codPostal', models.IntegerField(verbose_name='Codigo postal')),
                ('servicioRx', models.BooleanField(default=False, verbose_name='Servicio RX')),
                ('servicioFluoro', models.BooleanField(default=False, verbose_name='Servicio Fluoro')),
                ('servicioArococ', models.BooleanField(default=False, verbose_name='Servicio ArocoC')),
            ],
        ),
        migrations.CreateModel(
            name='Pacientes',
            fields=[
                ('id_pac', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=50, verbose_name='Apellido')),
                ('dni', models.IntegerField(verbose_name='Dni')),
                ('nacionalidad', models.CharField(max_length=50, verbose_name='Nacionalidad')),
                ('domicilio', models.CharField(max_length=50, verbose_name='Domicilio')),
                ('numero_domicilio', models.IntegerField(verbose_name='N° domicilio')),
                ('cobertura_medica', models.CharField(max_length=50, verbose_name='Cobertura Medica')),
                ('numero_afilido', models.IntegerField(verbose_name='N° afiliado')),
                ('sexo', models.CharField(max_length=20, verbose_name='Sexo')),
                ('fecha_nacimiento', models.DateField(verbose_name='Fecha de nacimiento')),
            ],
        ),
        migrations.AddField(
            model_name='estudio',
            name='instituciones',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.InstitucionMedica'),
        ),
        migrations.AddField(
            model_name='estudio',
            name='pacientes',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Pacientes'),
        ),
    ]
