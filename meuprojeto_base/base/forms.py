from django.forms import ModelForm, Form
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario, Item
from django import forms

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'username', 'email', 'password1', 'password2']

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'quantidade', 'armario', 'image', 'cautela', 'patrimônio']

