from django.test import TestCase
from django.urls import reverse, resolve
from django.test import SimpleTestCase
from admin_app.views import *
from django.test import TestCase
from django.test import TestCase, SimpleTestCase, Client

from django.urls import reverse, resolve

from products import views

from products.views import *
# Create your tests here.

class Testviews(TestCase):
    def test_views_pruchase(self):
        client=Client()
        url=reverse('purchase')
        response=client.post(url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,"users_purchases.html")

    def test_views_admin_dashboard(self):
            client = Client()
            url = reverse('dashboard')
            response = client.post(url)
            self.assertEquals(response.status_code,200)
            self.assertTemplateUsed(response, "admin_dashboard.html")




# Create your tests here.

class TestUrls(SimpleTestCase):
    def test_case_admindashboard_url(self):
        url=reverse("dashboard")
        print(resolve(url))
        self.assertEquals(resolve(url).func,admindashboard)

    def test_case_addadmin_url(self):
        url=reverse("addadmin")
        print(resolve(url))
        self.assertEquals(resolve(url).func,addadmins)

    def test_case_C_details_url(self):
        url=reverse("customers")
        print(resolve(url))
        self.assertEquals(resolve(url).func,C_details)

    def test_case_login_url(self):
        url=reverse("login")
        print(resolve(url))
        self.assertEquals(resolve(url).func,adminlogin)

    def test_case_logout_url(self):
        url=reverse("logout")
        print(resolve(url))
        self.assertEquals(resolve(url).func,signout)

    def test_case_products_url(self):
        url=reverse("products")
        print(resolve(url))
        self.assertEquals(resolve(url).func,p_details)