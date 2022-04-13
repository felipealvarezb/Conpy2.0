from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Dato
from .forms import DatoForm

@login_required(login_url="/login/")
def home(request):
    return render(request, "negocio/home.html")

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
    return render(request, "negocio/crud/editar.html")

@login_required(login_url="/login/")
def eliminar(request, id):
    datos = Dato.objects.get(id=id)
    datos.delete()
    return redirect('ingresos')
