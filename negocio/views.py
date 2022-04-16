from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Dato, Notificacion
from django.core.mail import send_mail
from .forms import DatoForm, NotificacionForm
from negocio.notificaciones import manejoNoti as mn

@login_required(login_url="/login/")
def home(request):
    return render(request, "negocio/home.html")

@login_required(login_url="/login/")
def notificaciones(request):
    msg=None
    datos=Notificacion.objects.all()
    formulario = NotificacionForm(request.POST or None)
    print(request.POST.get('fecha_lim'))
    if formulario.is_valid():
        formulario.save()
        descripcion=request.POST.get('descripcion')
        fecha=request.POST.get('fecha_lim')
        try:
            #mn.enviar_mail_nueva_noti(descripcion,fecha)
            msg="La notificación se ha creado correctamente"
        except:
            msg="hubo un error"
       

    return render(request,'negocio/notificaciones.html',{'datos':datos,'formulario':formulario,'msg':msg})

@login_required(login_url="/login/")
def perfil(request):
    return render(request,"negocio/perfil.html")

@login_required(login_url="/login/")
def ingresos(request):
    datos = Dato.objects.all()
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
