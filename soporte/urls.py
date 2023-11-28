from django.urls import path
from . import views


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('soportes/', views.soportes, name='soportes'),
    path('clientes', views.clientes, name='clientes')

]
