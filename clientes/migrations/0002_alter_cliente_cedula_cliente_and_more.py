# Generated by Django 4.0.3 on 2022-04-19 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cedula_cliente',
            field=models.IntegerField(verbose_name='cedula_cliente'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='celular_cliente',
            field=models.IntegerField(verbose_name='celular_cliente'),
        ),
    ]