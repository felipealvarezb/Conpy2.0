from django.shortcuts import render
from .models import Cliente
from .forms import ClienteForm
from django.shortcuts import render, redirect
# Create your views here.
def clientes_page(request):
    return render (request,'negocio/clientes.html')


def clientes(request):
    msg=None
    datos=Cliente.objects.all()
    formulario=ClienteForm(request.POST or None)
    if formulario.is_valid():
        try:
            formulario.save()
            msg='El cliente se ha creado correctamente'
        except:
            msg='Hubo un error al momneto de crear un cliente'
    return render(request,'negocio/clientes.html',{'datos':datos,'formulario':formulario,'msg':msg})

def eliminar(request, id):
    datos = Cliente.objects.get(id=id)
    datos.delete()
    return redirect('clientes')

def buscar_dato(request):
    ingreso=request.POST.get('busqueda')
    try:
        dato=int(ingreso)
        p= Cliente.objects.values_list('cedula_cliente','celular_cliente')
        for j in range(len(p)):
            datos=Cliente.objects.filter(cedula_cliente=ingreso)
            
            datos=Cliente.objects.filter(celular_cliente=ingreso)

    except:
        dato=str(ingreso)
        p= Cliente.objects.values_list('nombre_cliente','correo_cliente')
    

    for j in range(len(p)): #mejorar la complejidad
        pass
    
    msg=None
    #datos=Cliente.objects.filter(cedula_cliente=ingreso)
    formulario=ClienteForm(request.POST or None)
    return render(request,'negocio/clientes.html',{'datos':datos,'formulario':formulario,'msg':msg})