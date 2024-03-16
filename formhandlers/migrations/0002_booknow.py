# Generated by Django 5.0.3 on 2024-03-16 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formhandlers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookNow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('service_selected', models.CharField(max_length=100)),
            ],
        ),
    ]
