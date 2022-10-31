# Generated by Django 4.1.1 on 2022-10-27 00:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0004_alter_patients_eps'),
        ('clinic_history', '0002_remove_history_cc_remove_history_direction_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='Name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Patient.patients', verbose_name='Nombre'),
        ),
    ]