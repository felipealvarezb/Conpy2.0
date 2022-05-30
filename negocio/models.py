from datetime import date
from ssl import Options
from tabnanny import verbose
from django.db import models

class Dato(models.Model):
    options = (
        ('Ingreso', 'Ingreso'),
        ('Gasto', 'Gasto'),
    )
    id = models.AutoField(primary_key=True)
    fecha_creacion= models.DateTimeField(auto_now_add=True, blank=True,verbose_name='Fecha')
    movimiento = models.CharField(max_length=7, choices=options, verbose_name='Movimiento', null=True)
    nombre_tercero=models.TextField(max_length=35,verbose_name='Tercero',default=None, error_messages={'blank':'El tercero que ingresaste no existe'})
    valor = models.FloatField( verbose_name='Valor')
    descripcion = models.TextField(max_length=200,  verbose_name='Descripcion')
    
    def __str__(self):
        fila = "Movimiento: " + self.movimiento +" - "+ "Valor: " + str(self.valor)
        return fila
    
class Notificacion(models.Model):
    options=(
        ('Notificacion','notificacion')
    )
    id = models.AutoField(primary_key=True)
    descripcion = models.TextField(max_length=200,  verbose_name='Descripcion')
    fecha_lim = models.DateField(verbose_name='Fecha_lim')

    def __str__(self):
        fila='Descripcion: '+self.descripcion + ' -' + 'Fecha_Limite: '+ self.fecha_lim
        return fila
