from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    #path('clientes/', clientes_page, name="login"),
    path('clientes/',clientes,name='clientes'),
    path('eliminar_cliente/<int:id>',eliminar,name='eliminar_cliente'),
    #path('clientes/buscar/',buscar_dato,name='buscar_dato'),

]
