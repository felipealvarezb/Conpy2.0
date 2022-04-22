from django.db import models

class Cliente(models.Model):
    options = (
        ('Cliente', 'Cliente')
    )
    id = models.AutoField(primary_key=True)
    nombre_cliente=models.TextField(max_length=35,verbose_name='nombre cliente')
    cedula_cliente=models.IntegerField (verbose_name='cedula cliente')
    correo_cliente=models.EmailField(max_length=35,verbose_name='correo cliente')
    celular_cliente=models.IntegerField (verbose_name='celular cliente')
    
    def __str__(self):
        fila='Nombre: '+self.nombre_cliente+'- Cedula: '+self.cedula_cliente + '- Correo: '+self.cedula_cliente+'- Celular: '+self.celular_cliente
        return fila
    