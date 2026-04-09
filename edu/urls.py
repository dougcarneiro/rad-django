from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    # autor
    path('autor/create/', views.create_autor, name='create_autor'),
    path('autor/list/', views.list_autores, name='list_autores'),
    path('autor/<int:pk>/edit/', views.edit_autor, name='edit_autor'),
    
    # editora
    path('editora/create/', views.create_editora, name='create_editora'),
    path('editora/list/', views.list_editoras, name='list_editoras'),
    path('editora/<int:pk>/edit/', views.edit_editora, name='edit_editora'),
    
    # livro
    path('livro/create/', views.create_livro, name='create_livro'),
    path('livro/list/', views.list_livros, name='list_livros'),
    path('livro/<int:pk>/edit/', views.edit_livro, name='edit_livro'),
]