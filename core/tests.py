from django.test import TestCase

# Create your tests here.
# core/tests.py
from django.urls import reverse

class SimpleViewTest(TestCase):
    def test_home_page(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Welcome')