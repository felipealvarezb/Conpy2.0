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