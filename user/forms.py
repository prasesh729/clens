from user.models import User
from django import forms

class CustomerForm(forms.ModelForm):
    class Meta:
        model= User
        fields=['username','first_name','last_name','email']
