from django.db import models

class Tercero(models.Model):
    options = (
        ('Tercero', 'Tercero')
    )
    id = models.AutoField(primary_key=True)
    tipo_tercero=models.TextField(max_length=35,verbose_name='tipo tercero')
    nombre_tercero=models.TextField(max_length=35,verbose_name='nombre tercero')
    cedula_tercero=models.IntegerField (verbose_name='cedula tercero')
    correo_tercero=models.EmailField(max_length=35,verbose_name='correo tercero')
    celular_tercero=models.IntegerField (verbose_name='celular tercero')
    
    def __str__(self):
        fila='Tipo: '+self.tipo_tercero+'- Nombre: '+self.nombre_tercero+'- Cedula: '+self.cedula_tercero + '- Correo: '+self.cedula_tercero+'- Celular: '+self.celular_tercero
        return fila
