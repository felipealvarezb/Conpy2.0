# Generated by Django 4.0.3 on 2022-04-22 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('terceros', '0003_alter_tercero_tipo_tercero'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tercero',
            name='tipo_tercero',
        ),
    ]