from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('terceros/',terceros,name='terceros'),
    path('eliminar-tercero/<int:id>',eliminar_tercero,name='eliminar_tercero'),
    path('terceros/buscar/',buscar_dato,name='buscar_dato'),
]