from django.shortcuts import render
from .models import Tercero
from .forms import TerceroForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required(login_url="/login/")
def terceros(request):
    msg=None
    datos=Tercero.objects.all()
    Mayusculas=request.POST
    formulario=TerceroForm(request.POST or None)
    if formulario.is_valid():
        try:
            formulario.save()
            msg='El cliente se ha creado correctamente'
        except:
            msg='Hubo un error al momento de crear un cliente'
    return render(request,'negocio/terceros/terceros.html',{'datos':datos,'formulario':formulario,'msg':msg})

def eliminar_tercero(request, id):
    datos = Tercero.objects.get(id=id)
    datos.delete()
    return redirect('terceros')

def buscar_dato(request):
    volver=None #variable para definir si la pagina tiene el boton de volver o no
    no_esta=None #variable para definir si se abre la pagina de no se encontró alguna busqueda, si es != de None no se encontró algo 
    ingreso=request.POST.get('busqueda')
    print(ingreso)
    if ingreso!=' ':

        try:
            dato=int(ingreso)
            p= Tercero.objects.values_list('cedula_tercero','celular_tercero')
            for i in p:
                if Tercero.objects.filter(cedula_tercero__icontains=dato):
                    datos=Tercero.objects.filter(cedula_tercero__icontains=dato)
                    volver='a'
                    
                elif Tercero.objects.filter(celular_tercero__icontains=dato):
                    datos=Tercero.objects.filter(celular_tercero__icontains=dato)
                    volver='a' 
                    
                else:
                    volver='a'   
                    no_esta='no'     
        except ValueError:
            dato=str(ingreso)
            p= Tercero.objects.values_list('tipo_tercero','nombre_tercero','correo_tercero')
            for i in p:
                if Tercero.objects.filter(tipo_tercero__icontains=dato):
                    datos=Tercero.objects.filter(tipo_tercero__icontains=dato)
                    volver='a'
                    
                elif Tercero.objects.filter(nombre_tercero__icontains=dato):

                    datos=Tercero.objects.filter(nombre_tercero__icontains=dato)
                    print('lo contiene')
                    volver='a'
                    
                elif Tercero.objects.filter(correo_tercero__icontains=dato):
                    datos=Tercero.objects.filter(correo_tercero__icontains=dato)
                    volver='a'
                    
                else:
                    volver='a'
                    no_esta='no'
        try:
            return render(request,'negocio/terceros/terceros.html',{'datos':datos,'volver':volver})
        except UnboundLocalError:
            return render(request,'negocio/terceros/terceros.html',{'volver':volver,'esta':no_esta})
    else:   
        volver='a'          
        no_esta='no'   
        return render(request,'negocio/terceros/terceros.html',{'volver':volver,'esta':no_esta})