from django.shortcuts import render

# Create your views here.
def clientes_page(request):
    return render (request,'negocio/clientes.html')