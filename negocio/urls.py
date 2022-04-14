
from django.contrib import admin
from django.urls import path,re_path
from negocio import views as nviews


urlpatterns = [
    path('', nviews.home, name="home"),
    path('ingresos/', nviews.ingresos, name="ingresos"),
    path('ingresos/editar/', nviews.editar, name="editar"),   
    path('eliminar/<int:id>', nviews.eliminar, name="eliminar"),
    path('ingresos/editar/<int:id>', nviews.editar, name="editar"), 
    path('perfil/',nviews.perfil,name='perfil'), 
    path('notificaciones/',nviews.notificaciones,name='notificaciones',),
    path('eliminar_noti/<int:id>',nviews.eliminar_noti,name=('eliminar_noti'))
]