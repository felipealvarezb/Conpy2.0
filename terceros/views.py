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

def eliminar_tercero(request, id):
    datos = Tercero.objects.get(id=id)
    datos.delete()
    return redirect('terceros')

def buscar_dato(request):
    volver=None
    ingreso=request.POST.get('busqueda')
    try:
        dato=int(ingreso)
        p= Tercero.objects.values_list('cedula_tercero','celular_tercero')
        for i in p:
            if i[0]==dato:
                print('es una cedula') 
                datos=Tercero.objects.filter(cedula_tercero=dato)
                volver='a'
                
            elif i[1]==dato:
                print('es un celularrrrr')
                datos=Tercero.objects.filter(celular_tercero=dato)
                volver='a'
                
            else:
                print('no vi nada')         
    except:
        dato=str(ingreso)
        p= Tercero.objects.values_list('tipo_tercero','nombre_tercero','correo_tercero')
        for i in p:
            if i[0]==dato:
                print('es de tipo') 
                datos=Tercero.objects.filter(cedula_tercero=dato)
                volver='a'
                
            elif i[1]==dato:
                print('es un nombre')
                datos=Tercero.objects.filter(nombre_tercero=dato)
                volver='a'
                
            elif i[2]==dato:
                print('es un correo')
                datos=Tercero.objects.filter(correo_tercero=dato)
                volver='a'
                
            else:
                print('no vi nada') 
    return render(request,'negocio/terceros/terceros.html',{'datos':datos,'volver':volver})