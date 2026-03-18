from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.utils import timezone

# Create your views here.
def welcome(request):
    return HttpResponse('Bem-vindo ao meu blog!')

def eco(request, text):
    return HttpResponse(f'Você digitou: {text}')

def info(request):
    info = {
        "disciplina": "RAD",
        "framework": "Django",
        "semestre": "2025.2"
    }
    return JsonResponse(info)

def home(request):
    is_logged_in = request.user.is_authenticated
    role = 'admin' if is_logged_in and request.user.is_staff else 'user'

    contexto = {
        "usuario": "Douglas",
        "data_atual": timezone.now(),
        "is_logged_in": is_logged_in,
        "role": role,
    }
    return render(request, 'blog/home.html', contexto)


def contato(request, telefone):
    contexto = {
        "telefone": telefone,
    }
    return render(request, 'blog/contato.html', contexto)


def loops(request):
    produtos = [
        {"nome": "Notebook", "preco": 3500.00},
        {"nome": "Mouse", "preco": 120.50},
        {"nome": "Teclado", "preco": 210.90},
    ]
    contexto = {
        "produtos": produtos,
    }
    return render(request, 'blog/loops.html', contexto)