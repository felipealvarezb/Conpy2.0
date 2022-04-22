from django.shortcuts import render
from .models import Tercero
from .forms import TerceroForm
from django.shortcuts import render, redirect

def terceros(request):
    msg=None
    datos=Tercero.objects.all()
    formulario=TerceroForm(request.POST or None)
    if formulario.is_valid() and request.POST.get('tipo')!='SELECCIONAR':
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