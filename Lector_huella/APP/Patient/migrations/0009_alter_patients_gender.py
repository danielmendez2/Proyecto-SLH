# Generated by Django 4.1.1 on 2022-11-13 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0008_patients_rh'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patients',
            name='gender',
            field=models.CharField(max_length=12, verbose_name='Genero'),
        ),
    ]
