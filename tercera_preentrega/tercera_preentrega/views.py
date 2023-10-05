from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader

def inicio(request):
    return HttpResponse("comienzo, de proyecto")

def disco(request, nombre):
    return HttpResponse(f"El disco{nombre}")

def probando_template(request):
    
    nombre="El Salmon"
    autor="Andres Calamaro"
    año="1998"
    diccionario={"Nombre":nombre, "Autor": autor}

    # Abrimos el archivo html
    mi_html = open('./tercera_preentrega/plantillas/index.html')

    # Creamos el template haciendo uso de la clase Template
    plantilla = Template(mi_html.read())

    # Cerramos el archivo previamente abierto, ya que lo tenemos cargado en la variable plantilla
    mi_html.close()

    # Creamos un contexto, más adelante vamos a aprender a usarlo, ahora lo necesitamos aunque sea vacío para que funcione
    mi_contexto = Context()

    # Terminamos de construír el template renderizándolo con su contexto
    documento = plantilla.render(mi_contexto)

    return HttpResponse(documento)