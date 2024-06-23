from django import forms
from django.forms import modelform_factory, DecimalField
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput
from django.forms.widgets import Select

from .models import Product, GoITeens

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'new', 'rating']


GoITeenForm = modelform_factory(GoITeens,
  fields=('title', 'content', 'price', 'rubric'),
  labels={'title': 'Name good'},
  help_texts={'rubric': 'Create it!'},
  field_classes={'price': DecimalField},
  widgets={'rubric': Select(attrs={'size': 8})})


class RegisterUserForm(UserCreationForm):
  username = forms.CharField(
    max_length=50,
    widget=forms.TextInput(attrs={'class': 'form-control'})
  )
  email = forms.EmailField(
    widget=forms.EmailInput(attrs={'class': 'form-control'})
  )
  password1 = forms.CharField(
    max_length=250,
    widget=forms.PasswordInput(attrs={'class': 'form-control'})
  )
  password2 = forms.CharField(
    max_length=250,
    widget=forms.PasswordInput(attrs={'class': 'form-control'})
  )

  class Meta:
    model = User
    fields = ('username', 'email', 'password1', 'password2')





class LoginForm(AuthenticationForm):
  username = forms.CharField(widget=TextInput(attrs={'class': 'form-control'}))
  password = forms.CharField(widget=PasswordInput(attrs={'class': 'form-control'}))
