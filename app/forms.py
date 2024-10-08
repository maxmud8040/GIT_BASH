from django import forms
from .models import *


class ContactForm(forms.ModelForm):
    name = forms.CharField()

    class Meta:
        model = Contact
        fields = '__all__'