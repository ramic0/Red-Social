from django.shortcuts import render, redirect, get_object_or_404
from .models import Post,Perfil, FollowersCount
from .forms import PostForm
from django.utils import timezone
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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
def follow(request):
    if request.method== 'POST':
        follower = request.POST['follower']
        user = request.POST['user']
        if FollowersCount.objects.filter(follower=follower, user=user).first():
            delete_follower = FollowersCount.objects.get(follower=follower, user=user)
            delete_follower.delete()
            return redirect('accounts/profile/'+ user)
        else:
            new_follower = FollowersCount.objects.create(follower=follower, user=user)
            new_follower.save()
            return redirect('accounts/profile/'+ user)
    else:
        return redirect('home')



def editarPerfil(request):
    return render(request, 'base/editarPerfil.html')

