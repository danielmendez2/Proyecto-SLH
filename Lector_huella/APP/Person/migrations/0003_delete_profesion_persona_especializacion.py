# Generated by Django 4.1.1 on 2022-10-13 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctor', '0002_remove_medico_profesion'),
        ('Person', '0002_profesion_alter_persona_options'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profesion',
        ),
        migrations.AddField(
            model_name='persona',
            name='especializacion',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
    ]
