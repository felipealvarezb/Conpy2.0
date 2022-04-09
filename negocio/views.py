from django.shortcuts import render, redirect
from .models import Dato
from .forms import DatoForm

def home(request):
    return render(request, "negocio/home.html")

def ingresos(request):
    datos = Dato.objects.all()
    formulario = DatoForm(request.POST or None) 
    
    if formulario.is_valid():
        formulario.save()
    return render(request, "negocio/crud/ingresos.html", {'datos': datos, 'formulario': formulario})

def editar(request):
    return render(request, "negocio/crud/editar.html")

def eliminar(request, id):
    datos = Dato.objects.get(id=id)
    datos.delete()
    return redirect('ingresos')
