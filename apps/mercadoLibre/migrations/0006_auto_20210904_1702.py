# Generated by Django 3.2.5 on 2021-09-04 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mercadoLibre', '0005_remove_mercadolibre_codigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mercadolibre',
            name='imagen',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='mercadolibre',
            name='precio',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='mercadolibre',
            name='titulo',
            field=models.TextField(),
        ),
    ]
