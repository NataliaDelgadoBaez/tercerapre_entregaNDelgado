from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return render(request, "Tienda_app/index.html")

def discos(request):
    return render(request, "Tienda_app/discos.html")

def discos_comprados(request):
    return render(request, "Tienda_app/discos comprados.html")

def discos_vendidos(request):
    return render(request, "Tienda_app/discos vendidos.html")

def usuarios(request):
    return render(request, "Tienda_app/usuarios.html")