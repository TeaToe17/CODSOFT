from django import forms
from django.forms import ModelForm
from .models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ("name","number","email","address",)

class SearchForm(forms.Form):
    query = forms.CharField(label="Search",max_length=100)
    