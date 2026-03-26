from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome
    
class Editora(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome

class Livro(models.Model):
    autores = models.ManyToManyField(Autor, related_name='publicacoes')
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13, unique=True)
    publicacao = models.DateField()
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    estoque = models.IntegerField()
    
    def __str__(self):
        return self.titulo
    
    def listar_autores(self):
        return ', '.join(autor.nome for autor in self.autores.all())