# Generated by Django 5.0.3 on 2024-03-17 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formhandlers', '0003_patientinfo_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientinfo',
            name='sex',
            field=models.CharField(default='Not specified', max_length=20),
        ),
    ]