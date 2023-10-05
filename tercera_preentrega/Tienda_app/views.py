from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return render(request, "AppCoder/index.html")

def discos(request):
    return HttpResponse("Vista discos")

def discos_comprados(request):
    return HttpResponse("Vista discos comprados")

def discos_vendidos(request):
    return HttpResponse("Vista discos vendidos")

def usuarios(request):
    return HttpResponse("Vista usuarios")