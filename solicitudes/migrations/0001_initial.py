# Generated by Django 4.1.7 on 2023-03-27 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tecnicos', '0001_initial'),
        ('empleados', '0003_alter_empleado_ci'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solucion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fallas_reales', models.CharField(max_length=255)),
                ('solucion_realizada', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'Solucion',
            },
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_equipo', models.CharField(max_length=50)),
                ('problema', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=255)),
                ('fecha_creacion', models.DateField(auto_now=True)),
                ('estado', models.CharField(max_length=20)),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empleados.empleado')),
                ('solucion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='solicitudes.solucion')),
                ('tecnico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tecnicos.tecnico')),
            ],
            options={
                'db_table': 'Solicitud',
            },
        ),
        migrations.CreateModel(
            name='Repuesto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=100)),
                ('solucion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='solicitudes.solucion')),
            ],
            options={
                'db_table': 'Repuesto',
            },
        ),
    ]