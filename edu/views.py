from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from rest_framework import viewsets, permissions
from .serializers import AutorSerializer, EditoraSerializer    
from .forms import AutorForm, EditoraForm, LivroForm
from .models import Autor, Editora, Livro


@login_required
def home(request):
    return render(request, 'home.html')


@permission_required('edu.add_autor')
def create_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('edu:list_autores')
    else:
        form = AutorForm()
    return render(request, 'edu/create_autor.html', {'form': form})

@login_required
def list_autores(request):
    autores = Autor.objects.all()
    form = AutorForm()
    return render(request, 'edu/list_autores.html', {'autores': autores, 'form': form})


@permission_required('edu.change_autor')
def edit_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('edu:list_autores')
    else:
        form = AutorForm(instance=autor)
    return render(request, 'edu/edit_autor.html', {'form': form})

@permission_required('edu.add_editora')
def create_editora(request):
    if request.method == 'POST':
        form = EditoraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('edu:list_editoras')
    else:
        form = EditoraForm()
    return render(request, 'edu/create_editora.html', {'form': form})

@permission_required('edu.change_editora')
def edit_editora(request, pk):
    editora = get_object_or_404(Editora, pk=pk)
    if request.method == 'POST':
        form = EditoraForm(request.POST, instance=editora)
        if form.is_valid():
            form.save()
            return redirect('edu:list_editoras')
    else:
        form = EditoraForm(instance=editora)
    return render(request, 'edu/edit_editora.html', {'form': form})

@login_required
def list_editoras(request):
    editoras = Editora.objects.all()
    form = EditoraForm()
    return render(request, 'edu/list_editoras.html', {'editoras': editoras, 'form': form})

@permission_required('edu.add_livro')
def create_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('edu:list_livros')
    else:
        form = LivroForm()
    return render(request, 'edu/create_livro.html', {'form': form})

@login_required
def list_livros(request):
    livros_list = Livro.objects.all().order_by('-titulo')
    paginator = Paginator(livros_list, 10)
    page_number = request.GET.get('page')
    livros = paginator.get_page(page_number)
    form = LivroForm()
    return render(request, 'edu/list_livros.html', {'livros': livros, 'form': form})

@permission_required('edu.change_livro')
def edit_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('edu:list_livros')
    else:
        form = LivroForm(instance=livro)
    return render(request, 'edu/edit_livro.html', {'form': form})

@permission_required('edu.delete_livro')
def delete_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == 'POST':
        livro.delete()
        return redirect('edu:list_livros')
    return render(request, 'edu/delete_livro.html', {'livro': livro})

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    permission_classes = [permissions.AllowAny]
    
class EditoraViewSet(viewsets.ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer
    permission_classes = [permissions.AllowAny]