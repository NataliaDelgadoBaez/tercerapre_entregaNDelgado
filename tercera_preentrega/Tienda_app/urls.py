from django.urls import path
from Tienda_app import views

urlpatterns = [
    
    path('inicio/', views.inicio),
    path('disco/', views.discos, name="Discos"),
    path('discos_comprados/', views.discos_comprados),
    path('disco_vendidos/', views.discos_vendidos),
    path('usuarios/', views.usuarios),
    path('iniciar_sesion/', views.iniciar_sesion),
    path('crear_cuenta/', views.crear_cuenta),
    path('Discoform/', views.disco_formulario, name="Discoformulario"),
]
