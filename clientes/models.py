from django.db import models

class Cliente(models.Model):
    options = (
        ('Cliente', 'Cliente')
    )
    id = models.AutoField(primary_key=True)
    nombre_cliente=models.TextField(max_length=35,verbose_name='nombre_cliente')
    cedula_cliente=models.IntegerField (max_length=15,verbose_name='cedula_cliente')
    correo_cliente=models.TextField(max_length=35,verbose_name='correo_cliente')
    celular_cliente=models.IntegerField (max_length=15,verbose_name='celular_cliente')
    
    def __str__(self):
        fila='Nombre: '+self.nombre_cliente+'- Cedula: '+self.cedula_cliente + '- Correo: '+self.cedula_cliente+'- Celular: '+self.celular_cliente
        return fila
    