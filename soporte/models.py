from datetime import timezone
from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    documento = models.CharField(max_length=20, unique=True)
    direccion = models.TextField()
    correo = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre

class Soporte(models.Model):
    nombre_pc = models.CharField(max_length=100)
    descripcion_pc = models.TextField()
    descripcion_problema = models.TextField()
    prioridad = models.CharField(max_length=20, choices=[('Alta', 'Alta'), ('Media', 'Media'), ('Baja', 'Baja')])
    estado = models.CharField(max_length=20, choices=[('Abierto', 'Abierto'), ('En proceso', 'En proceso'), ('Cerrado', 'Cerrado')])
    fecha = models.DateTimeField(auto_now_add=True)
    cliente_id = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return f"Soporte para {self.nombre_pc}"
    

