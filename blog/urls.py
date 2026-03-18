from django.urls import path
from . import views

urlpatterns = [
    path('welcome/', views.welcome, name='welcome'),
    path('eco/<str:text>/', views.eco, name='eco'),
    path('info/', views.info, name='info'),
    path('home/', views.home, name='home'),
    path('contato/<str:telefone>/', views.contato, name='contato'),
    path('loops/', views.loops, name='loops'),
]