# Generated by Django 3.2.5 on 2021-09-08 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mercadoLibre', '0008_mercadolibre_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='mercadolibre',
            name='codigo',
            field=models.TextField(default='SOME STRING', max_length=250),
        ),
        migrations.AddField(
            model_name='mercadolibre',
            name='tienda',
            field=models.TextField(default='SOME STRING', max_length=250),
        ),
    ]
