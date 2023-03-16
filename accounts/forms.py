from django.forms import ModelForm
from base.models import Perfil
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class PerfilForm(ModelForm):
    class Meta:
        model = Perfil
        fields= ['name','email','bio','avatar']