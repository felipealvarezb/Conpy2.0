from typing import List
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Dato, Notificacion
from terceros.models import Tercero
from .forms import DatoForm, NotificacionForm

@login_required(login_url="/login/")
def home(request):
    return render(request, "negocio/home.html")

@login_required(login_url="/login/")
def notificaciones(request):
    """metodo para crear notificaciones 
    Args:
        request (_type_): cuando es llamado

    Returns:
        pagina: pagina de notificaciones con el dato nuevo
    """
    msg=None
    datos=Notificacion.objects.all()
    formulario = NotificacionForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        try:
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
    totalIngresos = list(Dato.objects.filter(movimiento='Ingreso').values())
    totalGastos = list(Dato.objects.filter(movimiento='Gasto').values())
    sumi = 0
    sumg = 0
    for valuei in totalIngresos:
        sumi = sumi + valuei['valor']
    
    for valueg in totalGastos:
        sumg = sumg + valueg['valor']
        

    proveedor=[]
    cliente=[]
    valido=False
    p=Tercero.objects.values_list('nombre_tercero','tipo_tercero')
    for i in p:
        if i[1]=='proveedor':
            proveedor.append(i[0])
            print(i[0], 'proveedor')
        elif i[1]=='cliente':
            cliente.append(i[0])

    if request.POST.get('movimiento')=='Gasto' and request.POST.get('nombre_tercero') in proveedor:
        valido=True
    elif request.POST.get('movimiento')=='Ingreso' and request.POST.get('nombre_tercero') in cliente:
        valido=True
    error=None
    if formulario.is_valid() and valido==True:
        formulario.save()
    else:
        error='No existe el tercero que ingresaste'
        print('hubo un error')
    return render(request, "negocio/crud/ingresos.html", {'datos': datos, 'formulario': formulario, 'sumi': sumi, 'sumg': sumg,'error':error})

@login_required(login_url="/login/")
def editar(request):
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


@login_required(login_url='/login/')
def clientes(request):
    return render(request,'negocio/clientes.html')
