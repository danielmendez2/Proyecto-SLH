# Generated by Django 4.1.1 on 2022-11-09 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic_history', '0005_rename_name_history_name_patients_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='Rh',
            field=models.CharField(blank=True, max_length=3, null=True, verbose_name='Rh'),
        ),
    ]
