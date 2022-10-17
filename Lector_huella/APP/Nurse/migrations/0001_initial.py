# Generated by Django 4.1.1 on 2022-10-17 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Person', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nurses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Professional_card', models.CharField(max_length=30, unique=True)),
                ('Specialization', models.CharField(max_length=100)),
                ('data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Person.people')),
            ],
            options={
                'verbose_name': 'Nurse',
            },
        ),
    ]
