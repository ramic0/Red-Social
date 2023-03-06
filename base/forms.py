from django.forms import ModelForm
from .models import Post
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class PostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ('user'),

#class UserRegisterForm(UserCreationForm):
#    email = forms.EmailField()
#    first_name = forms.CharField(label='Nombre')
#    last_name = forms.CharField(label='Apellido')
#    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
#    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)
#
#    class Meta:
#        model = User
#        fields = ['username','email','first_name','last_name','password1','password2']

# class UserLoginForm(AuthenticationForm):
#    username = forms.CharField(widget=forms.TextInput(
#        attrs={'class': 'form-control', 'placeholder': 'Username'}),
#        label="Username")
#    password = forms.CharField(widget=forms.PasswordInput(
#        attrs={'class': 'form-control', 'placeholder': 'Contraseña'}),
#        label="Contraseña")