from negocio.models import Notificacion
from django.core.mail import send_mail
from negocio.forms import NotificacionForm
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from datetime import *
from negocio.forms import DatoForm, NotificacionForm
def enviar_mail_nueva_noti(descripcion,fecha_lim):
    mensaje='Se ha creado una tarea con la siguiente descripcion:\n"'+descripcion+'"\nTiene como fecha limite:\n'+fecha_lim+"\naño/mes/dia"
    send_mail(
        'Se ha creado una tarea nueva',
        mensaje,
        settings.EMAIL_HOST_USER,
        ['jjsanchez1@hotmail.com'],
    )

def enviar_mail_fecha_cercana(descripcion,fecha_lim):
    fecha_limi=fecha_lim.strftime('%m/%d/%Y')
    #print(fecha_limi,'fecha enviar mail ')
    mensaje='Se acerca la fecha limite para la siguiente tarea:\n"'+descripcion+'"\nTiene como fecha limite:\n'+fecha_limi+"\nmes/dia/año"
    try:
        send_mail(
        'Tarea proxima en llegar al limite',
        mensaje,
        settings.EMAIL_HOST_USER,
        ['Conpyp1@gmail.com','jjsanchezps@outlook.com'],
        )      
        print('mandé correo')
    except:
        print('hubo un error')

def fecha_cercana(descripcion,fecha):
    fecha_caducada=None
    fa=date.today()#fecha actual
    fr=fecha-timedelta(days=2) #fecha para empezar a mandar notificaciones
    fdif=fr-fa #fecha de diferencia entre el dia actual y la fecha de mandar notificaciones
    fd=fdif.days
    if fd<=0 and fd>=-2:
        print(fecha)
        print("estoy entre la fecha de enviar notifiaciones")
        enviar_mail_fecha_cercana(descripcion,fecha)
        fecha_caducada=False
    elif fd<-2:
        fecha_caducada=True
        print('Fecha Vieja')
    else:
        fecha_caducada=False
        print('aun falta para la fecha')


def check_notificaciones_db():
    p = Notificacion.objects.values_list('descripcion','fecha_lim')
    for i in  p:
        fecha_cercana(i[0],i[1])