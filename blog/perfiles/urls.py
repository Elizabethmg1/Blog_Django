from django.urls import path
from perfiles import views

app_name = 'perfiles'

urlpatterns = [
    path('perfil/', views.perfil, name='perfil'),
    path('editarPerfil/', views.editarPerfil, name='editarPerfil'),
]