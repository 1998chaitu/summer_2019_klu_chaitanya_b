from onlineapp.forms import AddCollege
from onlineapp.models import *
from django import forms
from django.http import HttpResponse

class LoginForm(forms.Form):

    username = forms.CharField(max_length=30, required=True,
                               widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'enter username'})
                               )
    password = forms.CharField(max_length=30, required=True,
                               widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'enter password'})
                               )


class SignupForm(forms.Form):

    first_name = forms.CharField(max_length=30, required=True,
                                widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'enter firstname'})
                               )
    last_name = forms.CharField(max_length=30, required=True,
                               widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'enter lastname'})
                               )

    username = forms.CharField(max_length=30, required=True,
                               widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'enter username'})
                               )
    password = forms.CharField(max_length=30, required=True,
                               widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'enter password'})
                               )