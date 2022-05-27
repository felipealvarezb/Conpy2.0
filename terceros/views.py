from django.shortcuts import render
from .models import Tercero
from .forms import TerceroForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required(login_url="/login/")
def terceros(request):
    msg=None
    datos=Tercero.objects.all()
    formulario=TerceroForm(request.POST or None)
    if formulario.is_valid():
        try:
            formulario.save()
            msg='El cliente se ha creado correctamente'
        except:
            msg='Hubo un error al momento de crear un cliente'
    return render(request,'negocio/terceros/terceros.html',{'datos':datos,'formulario':formulario,'msg':msg})

@login_required(login_url="/login/")
def eliminar_tercero(request,id):
    datos = Tercero.objects.get(id=id)
    datos.delete()
    return redirect('terceros')

@login_required(login_url="/login/")
def buscar_dato(request):
    volver=None #variable para definir si la pagina tiene el boton de volver o no
    no_esta=None #variable para definir si se abre la pagina de no se encontró alguna busqueda, si es != de None no se encontró algo 
    ingreso=request.POST.get('busqueda')
    tipo=request.POST.get('filtro')
    if ingreso!=' ' and tipo!='TIPO':
        p=Tercero.objects.values_list(tipo)
        print(p)
        for i in p:
            try:
                a=int(ingreso)
                if tipo=='cedula_tercero' and Tercero.objects.filter(cedula_tercero__icontains=a):
                    datos=Tercero.objects.filter(cedula_tercero__icontains=a)
                elif tipo=='celular_tercero' and Tercero.objects.filter(celular_tercero__icontains=a):
                    datos=Tercero.objects.filter(celular_tercero__icontains=a)
                else:  
                    no_esta='no'
            except ValueError:
                if tipo=='tipo_tercero' and Tercero.objects.filter(tipo_tercero__icontains=ingreso):
                    datos=Tercero.objects.filter(tipo_tercero__icontains=ingreso)
                elif tipo=='nombre_tercero' and Tercero.objects.filter(nombre_tercero__icontains=ingreso):
                    datos=Tercero.objects.filter(nombre_tercero__icontains=ingreso)
                elif tipo=='correo_tercero' and Tercero.objects.filter(correo_tercero__icontains=ingreso):
                    datos=Tercero.objects.filter(correo_tercero__icontains=ingreso)
                else:  
                    no_esta='no'
            volver='a'
        try:
            return render(request,'negocio/terceros/terceros.html',{'datos':datos,'volver':volver})
        except UnboundLocalError:
            return render(request,'negocio/terceros/terceros.html',{'volver':volver,'esta':no_esta})
    else:   
        volver='a'          
        no_esta='no'   
        return render(request,'negocio/terceros/terceros.html',{'volver':volver,'esta':no_esta})

#arreglar todo eeste metodo
def editar_dato(request,id):
    datos = Tercero.objects.get(id=id)
    formulario = TerceroForm(request.POST or None) 
    proveedor=[]
    cliente=[]
    cambio_nombre=False
    error=None
    listo=None
    #p=Tercero.objects.values_list('nombre_tercero','tipo_tercero')

    for p in request.POST:
        
        if request.POST.get(p)!='SELECCIONAR'and p == 'tipo_tercero':
            if datos.tipo_tercero!=request.POST.get('tipo_tercero'):
                tipo_tercero=request.POST.get('tipo_tercero')
                Tercero.objects.select_for_update().filter(id=id).update(tipo_tercero=tipo_tercero)
                print('quiero un cambio en tercero',tipo_tercero)
                listo='se ha modificado correctamente'
            else:
                error='No has cambiado ningun dato'
        elif request.POST.get(p)!='' and p == 'nombre_tercero':
            nombre_tercero=request.POST.get('nombre_tercero')
            Tercero.objects.select_for_update().filter(id=id).update(nombre_tercero=nombre_tercero)
            listo='se ha modificado correctamente' 
        elif request.POST.get(p)!=''and p == 'cedula_tercero':
            cedula_tercero=request.POST.get('cedula_tercero')
            Tercero.objects.select_for_update().filter(id=id).update(cedula_tercero=cedula_tercero)
            listo='se ha modificado correctamente' 
        elif request.POST.get(p)!='' and p == 'correo_tercero' :
            correo_tercero=request.POST.get('correo_tercero')
            Tercero.objects.select_for_update().filter(id=id).update(correo_tercero=correo_tercero)
            listo='se ha modificado correctamente' 
        elif request.POST.get(p)!='' and p == 'celular_tercero' and len(request.POST.get(p))==10:
            
            celular_tercero=request.POST.get(p)
            Tercero.objects.select_for_update().filter(id=id).update(celular_tercero=celular_tercero)
            listo='se ha modificado correctamente'
        else:
            error='No has cambiado ningun dato'
        error='No has cambiado ningun dato'
    
    return render(request, "negocio/terceros/editar.html", {'formulario': formulario,'error':error,'listo':listo})