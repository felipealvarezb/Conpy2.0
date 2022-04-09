
from django.db import models

class Dato(models.Model):
    options = (
        ('Ingreso', 'Ingreso'),
        ('Gasto', 'Gasto'),
    )
    id = models.AutoField(primary_key=True)
    movimiento = models.CharField(max_length=7, choices=options, verbose_name='Movimiento', null=True)
    valor = models.FloatField( verbose_name='Valor')
    descripcion = models.TextField(max_length=200,  verbose_name='Descripcion')
    
    def __str__(self):
        fila = "Movimiento: " + self.movimiento +"-"+ "Descripcion: " + self.descripcion
        return fila
    
