from negocio.models import Notificacion
from django.core.mail import send_mail
from negocio.forms import NotificacionForm
from django.conf import settings
from django.core.mail import EmailMultiAlternatives


def enviar_mail():
    send_mail(
        'JUAN JOSE',
        'este es el primer correo desde CONPY',
        settings.EMAIL_HOST_USER,
        ['jjsanchez1@hotmail.com','jjsanchezc@eafit.edu.co'],
    )
