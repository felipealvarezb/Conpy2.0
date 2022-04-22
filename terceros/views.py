from django.shortcuts import render
from .models import Tercero
from .forms import TerceroForm
from django.shortcuts import render, redirect

def clientes_page(request):
    return render (request,'negocio/clientes.html')