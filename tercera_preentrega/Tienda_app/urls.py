from django.urls import path
from Tienda_app import views

urlpatterns = [
    
    path('inicio/', views.inicio),
    path('disco/', views.discos),
    path('disco/', views.discos_comprados),
    path('disco/', views.discos_vendidos),
    path('usuarios/', views.usuarios),
]
