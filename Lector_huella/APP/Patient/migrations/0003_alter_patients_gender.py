# Generated by Django 4.1.1 on 2022-10-24 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0002_alter_patients_cc_alter_patients_direction_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patients',
            name='gender',
            field=models.CharField(choices=[('F', 'FEMENINO'), ('M', 'MASCULINO'), ('O', 'OTRO')], max_length=1, verbose_name='Genero'),
        ),
    ]