from django.core.management.base import BaseCommand
from faker import Faker
from faker.providers import person, company, date_time
from edu.models import Autor, Editora, Livro

class Command(BaseCommand):
    help = 'Um comando de exemplo para demonstrar a criação'
    def handle(self, *args, **options):
        
        NUM_LIVROS = 10
        
        fake = Faker('pt_BR')
        fake.add_provider(person)
        fake.add_provider(company)
        fake.add_provider(date_time)
        
        isbn_list = []
        while len(isbn_list) < NUM_LIVROS:
            isbn = fake.isbn13()
            if isbn not in isbn_list:
                isbn_list.append(isbn)
    
        for i in range(NUM_LIVROS):
            autor = Autor.objects.create(nome=fake.name())
            editora = Editora.objects.create(nome=fake.company())
            livro = Livro.objects.create(
                titulo=fake.sentence(nb_words=4),
                isbn=isbn_list[i],
                publicacao=fake.date_this_decade(),
                preco=round(fake.random_number(digits=5) / 100, 2),
                estoque=fake.random_int(min=0, max=100),
                editora=editora,
            )
            livro.autores.add(autor)
            livro.save()
        