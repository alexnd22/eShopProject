from django import forms
from django.forms import TextInput, Textarea

from contact.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'subject', 'message']
        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'Please enter first name', 'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'Please enter last name', 'class': 'form-control'}),
            'email': TextInput(attrs={'placeholder': 'Please enter email', 'class': 'form-control'}),
            'subject': TextInput(attrs={'placeholder': 'Please enter subject', 'class': 'form-control'}),
            'message': Textarea(attrs={'placeholder': 'Please enter message', 'class': 'form-control'}),
        }
