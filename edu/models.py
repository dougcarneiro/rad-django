from django.db import models
from django.utils.translation import gettext_lazy as _

class Autor(models.Model):
    nome = models.CharField(_('nome'), max_length=100, unique=True)

    def __str__(self):
        return self.nome
    
class Editora(models.Model):
    nome = models.CharField(_('nome'), max_length=100, unique=True)

    def __str__(self):
        return self.nome

class Livro(models.Model):
    autores = models.ManyToManyField(Autor, related_name='publicacoes', verbose_name=_('autores'))
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE, verbose_name=_('editora'))
    titulo = models.CharField(_('título'), max_length=200)
    isbn = models.CharField(_('ISBN'), max_length=13, unique=True)
    publicacao = models.DateField(_('publicação'))
    preco = models.DecimalField(_('preço'), max_digits=6, decimal_places=2)
    estoque = models.IntegerField(_('estoque'))
    
    def __str__(self):
        return self.titulo
    
    def listar_autores(self):
        return ', '.join(autor.nome for autor in self.autores.all())
