# Generated by Django 5.1.4 on 2024-12-19 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Servicios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicio',
            name='imagen',
            field=models.ImageField(blank=True, upload_to='servicios'),
        ),
    ]
