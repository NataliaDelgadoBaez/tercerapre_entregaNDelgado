from django.shortcuts import render
from Tienda_app.models import Disco

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

def iniciar_sesion(request):
    return render(request, "Tienda_app/iniciar sesion.html")

def crear_cuenta(request):
    return render(request, "Tienda_app/crear cuenta.html")

def disco_formulario(request):
      if request.method == 'POST':
      
            disco =  Disco(request.post['disco'],(request.post['artista']))
 
            disco.save()
 
            return render(request, "Tienda_app/index.html")
 
      return render(request,"Tienda_app/Discoformulario.html")
