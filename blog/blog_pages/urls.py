from django.urls import path
from blog_pages import views

app_name = 'blog_pages'

urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('about/', views.acerca_de_mi, name='acerca_de_mi'),
    path('pages/', views.pages, name='leerpaginas'),
    path('pages/<pk>', views.leer_mas, name='leer_mas'),
    path('edit_page/<pk>', views.edit_page, name='edit_page'),
    path('delete_page/<pk>/', views.deletePage, name="delete_page"),
    path('create_page/', views.create_page, name="create_page"),
]