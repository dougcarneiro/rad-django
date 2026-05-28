from django.test import SimpleTestCase
from django.urls import reverse

class URLTestCase(SimpleTestCase):
    def test_home_url(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        
    