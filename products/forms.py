from products.models import Products,Booking
from django import forms

class ProductForm(forms.ModelForm):
    class Meta:
        model= Products
        fields="__all__"

class BookForm(forms.ModelForm):
  class Meta:
    model = Booking
    fields = ("__all__")