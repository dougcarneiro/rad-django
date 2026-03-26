from django.contrib import admin

from edu.models import Autor, Editora, Livro

# Register your models here.


class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    list_filter = ('nome',)
    search_fields = ('nome',)
    
class EditoraAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    list_filter = ('nome',)
    search_fields = ('nome',)
    
class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'listar_autores', 'editora', 'isbn', 'publicacao', 'preco', 'estoque')
    list_filter = ('autores', 'editora')
    search_fields = ('titulo', 'isbn')

    def listar_autores(self, obj):
        return ', '.join(autor.nome for autor in obj.autores.all())

    listar_autores.short_description = 'Autores'
    
admin.site.register(Autor, AutorAdmin)
admin.site.register(Editora, EditoraAdmin)
admin.site.register(Livro, LivroAdmin)

