# Generated by Django 4.1.1 on 2022-10-31 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nurse', '0002_alter_nurses_gender'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nurses',
            old_name='Cc',
            new_name='identification_number',
        ),
        migrations.AlterField(
            model_name='nurses',
            name='Eps',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='EPS'),
        ),
        migrations.AlterField(
            model_name='nurses',
            name='Specialization',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Especializacion'),
        ),
        migrations.AlterField(
            model_name='nurses',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de cumpleaños'),
        ),
        migrations.AlterField(
            model_name='nurses',
            name='gender',
            field=models.CharField(max_length=1, verbose_name='Genero'),
        ),
        migrations.AlterField(
            model_name='nurses',
            name='meets_the_profile',
            field=models.BooleanField(blank=True, null=True, verbose_name='Cumple con el perfil'),
        ),
    ]