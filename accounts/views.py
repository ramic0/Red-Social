from django.shortcuts import render, redirect,get_object_or_404
from base.models import Perfil,Post
from .models import Relationship
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from accounts.forms import PerfilForm
from django.contrib.auth.decorators import login_required

def signup(request):
        if request.method =='GET':
             return render(request, 'registration/signup.html',{'form':UserCreationForm})
        else:
             if request.POST['password1'] == request.POST['password2']:
                try:
                  user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                  user.save()
                  user_login = auth.authenticate(username=request.POST['username'], password=request.POST['password1'])
                  login(request, user_login)
                  user_model = User.objects.get(username=request.POST['username'])
                  new_perfil = Perfil.objects.create(user=user_model)
                  new_perfil.save()
                  return redirect('settings')
                except IntegrityError:
                    messages.info(request,'Usuario ya existe')
                    return render(request, 'registration/signup.html',{'form':UserCreationForm})
        messages.info(request,'Contrasela no coincide')
        return render(request, 'registration/signup.html',{'form':UserCreationForm})
                     
def signin(request):
    if request.method == 'GET':
        return render(request, 'registration/signup.html')
    else:
        user = authenticate(username = request.POST['username'],
                            password = request.POST['password'],
                           )
        if user is None:
            return render(request, 'signing.html', {'form':AuthenticationForm,'error':'Username or password is incorrect'})
        else:
            login(request, user)
            return redirect('muro')

@login_required
def settings(request):
    user_perfil = Perfil.objects.get(user=request.user)
    if request.method == 'POST':
        if request.FILES.get('avatar') == None:
            avatar = user_perfil.avatar
            name = request.POST['name']
            apellido = request.POST['apellido']
            email = request.POST['email']
            bio = request.POST['bio']

            user_perfil.name = name
            user_perfil.apellido = apellido
            user_perfil.email = email
            user_perfil.avatar = avatar
            user_perfil.bio = bio
            user_perfil.save()

        if request.FILES.get('avatar') != None:
            avatar = request.FILES.get('avatar')
            name = request.POST['name']
            apellido = request.POST['apellido']
            email = request.POST['email']
            bio = request.POST['bio']
            
            user_perfil.name = name
            user_perfil.apellido = apellido
            user_perfil.email = email
            user_perfil.avatar = avatar
            user_perfil.bio = bio
            user_perfil.save()
        return redirect('settings')
    return render(request, 'perfil/settings.html', {'user_perfil':user_perfil})

@login_required
def muro(request):
    #user_perfil = Perfil.objects.all()
    user_perfil = Perfil.objects.all()
    posts = Post.objects.all()
    return render(request, 'base/muro.html', {'posts': posts, 'user_pefil':user_perfil})

@login_required       
def ver_perfil(request):
    perfils= Perfil.objects.filter(user=request.user)
    return render(request, 'perfil/perfil.html', {'perfils':perfils})

def profile(request, username=None):
	current_user = request.user
	if username and username != current_user.username:
		user = Perfil.objects.get(user=request.user)
		posts = Post.objects.all()
	else:
		user = Perfil.objects.get(user=request.user)
		posts = Post.objects.all()
	return render(request, 'perfil/profile.html', {'user':user, 'posts':posts})

def follow(request, username):
	current_user = request.user
	to_user = User.objects.get(username=username)
	to_user_id = to_user
	rel = Relationship(from_user=current_user, to_user=to_user_id)
	rel.save()
	messages.success(request, f'sigues a {username}')
	return redirect('muro')

def unfollow(request, username):
	current_user = request.user
	to_user = User.objects.get(username=username)
	to_user_id = to_user.id
	rel = Relationship.objects.filter(from_user=current_user.id, to_user=to_user_id).get()
	rel.delete()
	messages.success(request, f'Ya no sigues a {username}')
	return redirect('muro')

@login_required   
def upload(request):
    if request.method == 'POST':
        user = request.user.username
        image = request.FILES.get('image_upload')
        caption = request.POST['caption']

        new_post = Post.objects.create(user=user, image=image, caption=caption)
        new_post.save()
        return redirect('muro')
    else:
        return redirect('muro')
    
@login_required
def signout(request):
    logout(request)
    return redirect('index')
