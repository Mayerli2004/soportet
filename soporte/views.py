from django.shortcuts import render
from .models import Cliente, Soporte

def inicio(request):
    return render(request, 'paginas/inicio.html', {'section': 'inicio'})

def soportes(request):
    soportes = Soporte.objects.all()
    return render(request, 'paginas/index.html', {'soportes': soportes})

def clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'paginas/clientes.html', {'clientes': clientes})