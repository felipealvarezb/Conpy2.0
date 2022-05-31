from tkinter import dialog
from typing import List
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Dato, Notificacion
from terceros.models import Tercero
from .forms import DatoForm, NotificacionForm
from .utils import get_plot

@login_required(login_url="/login/")
def home(request):
    #empieza tabla de ganancias mensuales
    qs=Dato.objects.all()
    x = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
    y=[]
    tmp=[]
    res=0
    for a in qs:
        if a.movimiento=='Gasto':
            valor=a.valor
            valor*=-1
            tmp.append([[valor],[a.fecha_creacion.month-1]])
        else:
            tmp.append([[a.valor],[a.fecha_creacion.month-1]])
    for i in range(len(x)):
        for j in range(len(tmp)):
            mes=tmp[j][1]
            mes=mes[0]
            if mes==i:
                valor=tmp[j][0]
                res+=valor[0]
                
        y.append(res)
        res=0
    mensual=get_plot(x,y,'Movimientos - Mensuales','Meses','Ganancias')
    #acaba tabla de ganancias mensuales
    
    #empieza tabla ganacias diarias
    x = ['Dom','Lun','Mar','Mie','Jue','Vie','Sab']
    
    y=[]
    tmp=[]
    res=0
    for a in qs:
        if a.movimiento=='Gasto':
            valor=a.valor
            valor*=-1
            tmp.append([[valor],[a.fecha_creacion.strftime("%w")]])
        else:
            tmp.append([[a.valor],[a.fecha_creacion.strftime("%w")]])
    for i in range(len(x)):
        for j in range(len(tmp)):
            dia=tmp[j][1]
            dia=dia[0]
            
            if int(dia)==i:
                print('entro en dia')
                valor=tmp[j][0]
                res+=valor[0]
                
        y.append(res)
        res=0
    #acaba tabla de ganancias diarias
    semanal=get_plot(x,y,'Movimientos - semanales','Meses','Ganancias')
    return render(request, "negocio/home.html",{'mensual':mensual,'semanal':semanal})

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
        
    sumtotal = sumi - sumg
    print(request.POST.get('id'))    

    proveedor=[]
    cliente=[]
    valido=False
    try:
        p=Tercero.objects.values_list('nombre_tercero','tipo_tercero')
        for i in p:
            if i[1]=='proveedor':
                proveedor.append(i[0])
                
            elif i[1]=='cliente':
                cliente.append(i[0])

        if request.POST.get('movimiento')=='Gasto' and request.POST.get('nombre_tercero') in proveedor:
            valido=True
        elif request.POST.get('movimiento')=='Ingreso' and request.POST.get('nombre_tercero') in cliente:
            valido=True
        error=None
        if formulario.is_valid() and valido==True:
            formulario.save()
            
        context = {'datos': datos, 'formulario': formulario, 'sumi': sumi, 'sumg': sumg,'sumtotal':sumtotal, 'error':error}
        return render(request, "negocio/crud/ingresos.html", context)
    
    except:  

        return render(request, "negocio/crud/ingresos.html", {'datos': datos, 'formulario': formulario, 'sumi': sumi, 'sumg': sumg})
    


@login_required(login_url="/login/")
def buscar_dato(request):
    volver=None #variable para definir si la pagina tiene el boton de volver o no
    no_esta=None #variable para definir si se abre la pagina de no se encontró alguna busqueda, si es != de None no se encontró algo 
    ingreso=request.POST.get('busqueda')
    print(ingreso)
    tipo=request.POST.get('filtro')
    print(tipo)
    if ingreso!=' ' and tipo!='TIPO':
        p=Dato.objects.values_list(tipo)
        #print(p)
        for i in p:
            try:
                a=float(ingreso)
                if tipo=='valor' and Dato.objects.filter(valor__icontains=a):
                    datos=Dato.objects.filter(valor__contains=a)
                else:  
                    no_esta='no'
            except ValueError:
                if tipo=='nombre_tercero' and Dato.objects.filter(nombre_tercero__icontains=ingreso):
                    datos=Dato.objects.filter(nombre_tercero__icontains=ingreso)
                elif tipo=='descripcion' and Dato.objects.filter(descripcion__icontains=ingreso):
                    datos=Dato.objects.filter(descripcion__icontains=ingreso)
                elif tipo=='movimiento' and Dato.objects.filter(movimiento__icontains=ingreso):
                    datos=Dato.objects.filter(movimiento__icontains=ingreso)
                else:  
                    no_esta='no'
            volver='a'
        try:
            return render(request,'negocio/crud/ingresos.html',{'datos':datos,'volver':volver})
        except UnboundLocalError:
            return render(request,'negocio/crud/ingresos.html',{'volver':volver,'esta':no_esta})
    else:   
        volver='a'          
        no_esta='no'   
        return render(request,'negocio/terceros/terceros.html',{'volver':volver,'esta':no_esta})

@login_required(login_url="/login/")
def editar(request,id):
    datos = Dato.objects.get(id=id)
    formulario = DatoForm(request.POST or None) 
    proveedor=[]
    cliente=[]
    cambio_nombre=False
    error=None
    listo=None
    p=Tercero.objects.values_list('nombre_tercero','tipo_tercero')
    for p in request.POST:
        if request.POST.get('movimiento')!='SELECCIONAR'and p == 'movimiento':
            if datos.movimiento!=request.POST.get('movimiento'):
                cambio_nombre=True
                movimiento=request.POST.get('movimiento')
                print('quiero un cambio en movimiento')
            else:
                error='No has cambiado ningun dato'
        elif request.POST.get('nombre_tercero')!=''and p == 'nombre_tercero':
            tercero=request.POST.get('nombre_tercero')
            a=Tercero.objects.values_list('nombre_tercero','tipo_tercero')
            for i in a:
                if i[1]=='proveedor':
                    proveedor.append(i[0])
                    
                elif i[1]=='cliente':
                    cliente.append(i[0])
            print('entro en el if')
            if datos.movimiento=='Gasto' and tercero in proveedor:
                Dato.objects.select_for_update().filter(id=id).update(nombre_tercero=tercero)
                listo='se ha modificado correctamente'
            elif datos.movimiento=='Ingreso' and tercero in cliente:
                Dato.objects.select_for_update().filter(id=id).update(nombre_tercero=tercero)
                listo='se ha modificado correctamente'
            elif datos.movimiento=='Ingreso' and tercero in proveedor and cambio_nombre==True:
                Dato.objects.select_for_update().filter(id=id).update(movimiento=movimiento,nombre_tercero=tercero)
                listo='se ha modificado correctamente'
            elif datos.movimiento=='Gasto' and tercero in cliente and cambio_nombre==True:
                Dato.objects.select_for_update().filter(id=id).update(movimiento=movimiento,nombre_tercero=tercero)
                listo='se ha modificado correctamente'
            else:
                error='No has cambiado ningun dato'
        elif request.POST.get('valor')!='' and p == 'valor':
            valor=request.POST.get('valor')
            Dato.objects.select_for_update().filter(id=id).update(valor=valor)
            listo='se ha modificado correctamente' 
        elif request.POST.get('descripcion')!='' and p == 'descripcion':
            mensaje=request.POST.get('descripcion')
            Dato.objects.select_for_update().filter(id=id).update(descripcion=mensaje)
            listo='se ha modificado correctamente'
        else:
            error='No has cambiado ningun dato'
        error='No has cambiado ningun dato'
    
    return render(request, "negocio/crud/editar.html", {'formulario': formulario,'error':error,'listo':listo})

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
