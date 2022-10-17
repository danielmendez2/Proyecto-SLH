# Generated by Django 4.1.1 on 2022-10-17 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Surname', models.CharField(max_length=50)),
                ('age', models.CharField(max_length=3)),
                ('Cc', models.CharField(max_length=11, unique=True)),
                ('Phone', models.CharField(max_length=13)),
                ('Direction', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=4)),
                ('Eps', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('date_of_birth', models.DateField()),
            ],
        ),
    ]
