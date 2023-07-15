from admin_app.views import *
from django.test import TestCase
from django.test import TestCase, SimpleTestCase, Client

from django.urls import reverse, resolve


class Testviews(TestCase):
    def test_views_product(self):
        client = Client()
        url = reverse('product')
        response = client.post(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "product.html")

    def test_views_admin_products(self):
        client = Client()
        url = reverse('login')
        response = client.post(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "login.html")