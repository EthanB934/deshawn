# Generated by Django 5.1.7 on 2025-03-17 18:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deshawnapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed', models.BooleanField(default=False)),
                ('date', models.DateField()),
                ('walker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='deshawnapi.walker')),
            ],
        ),
    ]
