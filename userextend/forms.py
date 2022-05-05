from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, SetPasswordForm, PasswordResetForm
from django.forms import TextInput, EmailInput

from userextend.models import UserExtend


class UserExtendForm(UserCreationForm):
    class Meta:
        model = UserExtend
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'username']
        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'Enter your first name', 'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'Enter your last name', 'class': 'form-control'}),
            'email': EmailInput(attrs={'placeholder': 'Enter your email', 'class': 'form-control'}),
            'username': TextInput(attrs={'placeholder': 'Enter your username', 'class': 'form-control'}),
            'phone': TextInput(attrs={'placeholder': 'Enter your phone', 'class': 'form-control'}),
            'address': TextInput(attrs={'placeholder': 'Enter your address', 'class': 'form-control'})

        }

    def __init__(self, *args, **kwargs):
        super(UserExtendForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Enter password'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Enter password confirmation'


class UserExtendUpdateForm(forms.ModelForm):
    class Meta:
        model = UserExtend
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'username']
        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'Enter your first name', 'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'Enter your last name', 'class': 'form-control'}),
            'email': EmailInput(attrs={'placeholder': 'Enter your email', 'class': 'form-control'}),
            'username': TextInput(attrs={'placeholder': 'Enter your username', 'class': 'form-control'}),
            'phone': TextInput(attrs={'placeholder': 'Enter your phone', 'class': 'form-control'}),
            'address': TextInput(attrs={'placeholder': 'Enter your address', 'class': 'form-control'})

        }

    def __init__(self, *args, **kwargs):
        super(UserExtendUpdateForm, self).__init__(*args, **kwargs)


class AuthenticationLoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter your username'}
        )
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter your password'}
        )


class SetPasswordCustomForm(SetPasswordForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['new_password1'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter your new password'}
        )
        self.fields['new_password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter your new password confirmation'}
        )


class PasswordResetCustomForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter your email'}
        )
