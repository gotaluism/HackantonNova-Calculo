# Generated by Django 4.2.1 on 2023-05-27 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='general',
            fields=[
                ('idEpik', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('mail', models.CharField(max_length=100)),
                ('curso', models.CharField(max_length=4)),
                ('monitoria', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='taller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaEntrega', models.DateField()),
                ('validado', models.BooleanField(default=False)),
                ('idEstudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.general')),
            ],
        ),
        migrations.CreateModel(
            name='montiria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreMonitor', models.CharField(max_length=100)),
                ('FechaMonitoria', models.DateTimeField()),
                ('validado', models.BooleanField(default=False)),
                ('idEpik', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.general')),
            ],
        ),
    ]