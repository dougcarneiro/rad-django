from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Um comando de exemplo para demonstrar a criação'
    def handle(self, *args, **options):
        # A lógica do seu comando vai aqui
        self.stdout.write("O comando foi executado com sucesso!")