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
        #dato=int(ingreso)
        p= Cliente.objects.values_list('cedula_cliente','celular_cliente')
        
        for i in range(len(p)):
            for j in p:
                print(j, ' este es j')
                if Cliente.objects.filter(cedula_cliente=dato) !=[]:
                    print('es una cedula la que se introdujo') 
                elif Cliente.objects.filter(celular_cliente=dato)!=[]:
                    print('se introdujo un celular')
                else:
                    print('no es nada')
                
    except:
        dato=str(ingreso)
        p= Cliente.objects.values_list('nombre_cliente','correo_cliente')
    print(type(dato))
    datos=Cliente.objects.filter(cedula_cliente=dato)
    msg=None
    formulario=ClienteForm(request.POST or None)
    return render(request,'negocio/clientes.html',{'datos':datos,'formulario':formulario,'msg':msg})