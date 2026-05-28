from django.test import TestCase, SimpleTestCase
from rest_framework.test import APIClient, APITestCase

from edu.models import Autor

class AutorTestCase(TestCase):
    def setUp(self):
        Autor.objects.create(nome="Gabriel García Márquez",)
        
    def test_autor_existe(self):
        autor = Autor.objects.get(nome="Gabriel García Márquez")
        self.assertEqual(autor.nome, "Gabriel García Márquez")
    
    def test_autor_nao_existe(self):
        with self.assertRaises(Autor.DoesNotExist):
            Autor.objects.get(nome="Jorge Luis Borges")

class AutorSerializerTestCase(TestCase):
    def test_autor_serializer(self):
        from edu.serializers import AutorSerializer
        form_data = {'nome': 'Isabel Allende'}
        serializer = AutorSerializer(data=form_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data['nome'], "Isabel Allende")

class AutorFormTestCase(TestCase):
    def test_autor_form(self):
        from edu.forms import AutorForm
        form_data = {'nome': 'Mario Vargas Llosa'}
        form = AutorForm(data=form_data)
        self.assertTrue(form.is_valid())
        
    def test_autor_form_invalido(self):
        from edu.forms import AutorForm
        form_data = {'nome': ''}
        form = AutorForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('nome', form.errors)
        
class APIAutorTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.autor = Autor.objects.create(nome="Chinua Achebe")
    
    def test_api_autor_list(self):
        from rest_framework.test import APIClient
        client = APIClient()
        response = client.get('/edu/api/autor/')
        self.assertEqual(response.status_code, 200)