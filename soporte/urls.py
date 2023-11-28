from django.urls import path
from . import views


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('soportes/', views.soportes, name='soportes'),
    path('clientes', views.clientes, name='clientes'),
    path('nuevo_cliente/', views.nuevo_cliente, name='nuevo_cliente'),
    path('nuevo_soporte/', views.nuevo_soporte, name='nuevo_soporte')
]
