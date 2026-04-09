from django.shortcuts import render, redirect
from .forms import AutorForm, EditoraForm, LivroForm
from .models import Autor, Editora, Livro

def home(request):
    return render(request, 'home.html')

def create_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('edu:list_autores')
    else:
        form = AutorForm()
    return render(request, 'edu/create_autor.html', {'form': form})

def list_autores(request):
    autores = Autor.objects.all()
    form = AutorForm()
    return render(request, 'edu/list_autores.html', {'autores': autores, 'form': form})

def edit_autor(request, pk):
    autor = Autor.objects.get(pk=pk)
    if request.method == 'POST':
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('edu:list_autores')
    else:
        form = AutorForm(instance=autor)
    return render(request, 'edu/edit_autor.html', {'form': form})

def create_editora(request):
    if request.method == 'POST':
        form = EditoraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('edu:list_editoras')
    else:
        form = EditoraForm()
    return render(request, 'edu/create_editora.html', {'form': form})

def edit_editora(request, pk):
    editora = Editora.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditoraForm(request.POST, instance=editora)
        if form.is_valid():
            form.save()
            return redirect('edu:list_editoras')
    else:
        form = EditoraForm(instance=editora)
    return render(request, 'edu/edit_editora.html', {'form': form})

def list_editoras(request):
    editoras = Editora.objects.all()
    form = EditoraForm()
    return render(request, 'edu/list_editoras.html', {'editoras': editoras, 'form': form})

def create_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('edu:list_livros')
    else:
        form = LivroForm()
    return render(request, 'edu/create_livro.html', {'form': form})

def list_livros(request):
    livros = Livro.objects.all()
    form = LivroForm()
    return render(request, 'edu/list_livros.html', {'livros': livros, 'form': form})

def edit_livro(request, pk):
    livro = Livro.objects.get(pk=pk)
    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('edu:list_livros')
    else:
        form = LivroForm(instance=livro)
    return render(request, 'edu/edit_livro.html', {'form': form})
