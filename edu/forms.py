from django import forms
from .models import Autor, Editora, Livro

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nome']
        
class EditoraForm(forms.ModelForm):
    class Meta:
        model = Editora
        fields = ['nome']

class LivroForm(forms.ModelForm):
    publicacao = forms.DateField(
        widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d']
    )

    class Meta:
        model = Livro
        fields = ['titulo', 'autores', 'editora', 'isbn', 'publicacao', 'preco', 'estoque']
        widgets = {
            'autores': forms.CheckboxSelectMultiple(),
        }