from django.urls import path
from .views import clientes_page
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('clientes/', clientes_page, name="login"),

]
