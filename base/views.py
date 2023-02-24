from django.shortcuts import render
from .models import Post,Perfil

# Create your views here.
def index(request):
    return render(request, 'base/index.html')

def dashboard(request):
    posts = Post.objects.all()
    return render(request, 'base/dashboard.html', {'posts':posts})

def perfil(request):
    return render(request, 'base/perfil.html', {})