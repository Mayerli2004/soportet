from django.shortcuts import render, redirect
from .models import Cliente, Soporte
from .form import ClienteForm, SoporteForm
from django.http import HttpResponse
from django.contrib import messages



def inicio(request):
    return render(request, 'paginas/inicio.html', {'section': 'inicio'})

def soportes(request):
    soportes = Soporte.objects.all()
    return render(request, 'paginas/index.html', {'soportes': soportes})

def clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'paginas/clientes.html', {'clientes': clientes})

def nuevo_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente registrado')
            return redirect('clientes')
    else:
        form = ClienteForm()

def nuevo_soporte(request):
    clientes = Cliente.objects.all()
    if request.method == 'POST':
        form = SoporteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Soporte registrado')
            return redirect('soportes')
    else:
        form = SoporteForm()

    return render(request, 'paginas/registrar_soporte.html', {'form': form, 'clientes': clientes})
