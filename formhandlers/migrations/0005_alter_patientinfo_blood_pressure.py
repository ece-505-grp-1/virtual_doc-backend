# Generated by Django 5.0.3 on 2024-03-17 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formhandlers', '0004_alter_patientinfo_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientinfo',
            name='blood_pressure',
            field=models.CharField(max_length=20),
        ),
    ]
