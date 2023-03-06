from django.shortcuts import render, redirect, get_object_or_404
from .models import Post,Perfil
from .forms import PostForm
from django.utils import timezone
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

def index(request):
    return render(request, 'base/home.html')

def listar_perfiles(request):
    lista_perfil = Perfil.objects.all()
    context = {
        'perfiles':lista_perfil
    }
    return render(request, 'base/perfiles.html', context)

def mostar_post_por_perfil(request, id):
    lista_posts = Post.objects.filter(user=id)
    context ={
        'posts':lista_posts
    }
    return render(request, 'base/postsPorPerfil.html', context)

def recuperar_perfil(request,id):
    perfil = Perfil.objects.get(id=id)
    context = {
        'perfil': perfil
    }
    return render(request, 'base/perfil.html', context)

@login_required
def crearPost(request):
    if request.method == 'GET':
        form = PostForm()
        context = {
            'form':form
        }
        return render(request, 'base/CrearPost.html', context)
    
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect('home')

def editarPerfil(request):
    return render(request, 'base/editarPerfil.html')

def login(request):
    return render(request, 'base/login.html',{})