from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Dato, Notificacion
from django.core.mail import send_mail
from .forms import DatoForm, NotificacionForm

@login_required(login_url="/login/")
def home(request):
    return render(request, "negocio/home.html")

@login_required(login_url="/login/")
def notificaciones(request):
    datos=Notificacion.objects.all()
    formulario = NotificacionForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
    return render(request,'negocio/notificaciones.html',{'datos':datos,'formulario':formulario})

@login_required(login_url="/login/")
def perfil(request):
    return render(request,"negocio/perfil.html")

@login_required(login_url="/login/")
def ingresos(request):
    datos = Dato.objects.all()
    print(datos)
    formulario = DatoForm(request.POST or None) 
    
    if formulario.is_valid():
        formulario.save()
    return render(request, "negocio/crud/ingresos.html", {'datos': datos, 'formulario': formulario})

@login_required(login_url="/login/")
def editar(request):
    #send_mail("este es el subjet",'este es el mensjaeeeee','jjsanchezc@eafit.edu.co',['jjsanchez1@hotmail.com'])
    return render(request, "negocio/crud/editar.html")

@login_required(login_url="/login/")
def eliminar(request, id):
    datos = Dato.objects.get(id=id)
    datos.delete()
    return redirect('ingresos')

@login_required(login_url="/login/")
def eliminar_noti(request,id):
    datos=Notificacion.objects.get(id=id)
    datos.delete()
    return redirect('notificaciones')
