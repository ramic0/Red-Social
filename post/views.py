from django.shortcuts import render, redirect, get_object_or_404
from base.models import Post
from .models import LikePost
from base.forms import PostForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import View

# Create your views here.

@login_required
def crearPost(request):
    if request.method == 'GET':
        form = PostForm()
        context = {
            'form':form
        }
        return render(request, 'base/CrearPost.html', context)
    else:
        try:
            form = PostForm(request.POST)
            nuevo_post= form.save(commit=False)
            nuevo_post.user = request.user
            nuevo_post.save()
            return redirect('ver_post')
        except ValueError:
            return render(request, 'base/CrearPost.html', {'form': PostForm})
        
@login_required
def ver_post(request):
    posts = Post.objects.filter(user=request.user)
    return render(request, 'post/ver_post.html', {'posts':posts})

@login_required
def post_detail(request,post_id):
    #if request.method == 'GET':
    #    print("log3")
    #    post = get_object_or_404(Post, pk=post_id, user=request.user)
    #    form = PostForm(instance=post)
    #    return render(request,'post/post_detail.html',{'post':post,'form':form})
    #else:
    post = get_object_or_404(Post, pk=post_id, user=request.user)
    form = PostForm(request.POST, instance=post)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            try:
                form.save()
                return redirect('ver_post')
            except ValueError:
                messages.info(request,'Error en la actulizacion de post')
    return render(request, 'post/post_detail.html',{'post':post,'form':form} )

@login_required
def post_delete(request,post_id):
    post = get_object_or_404(Post, pk=post_id, user=request.user)
    if request.method == 'POST':
        post.delete()
        return redirect('ver_post')
    
def like_post(request):
    username = request.user.username
    post_id = request.GET.get('post_id')

    post = Post.objects.get(id=post_id)

    like_filter = LikePost.objects.filter(post_id=post_id, username=username).first()

    if like_filter == None:
        new_like = LikePost.objects.create(post_id=post_id, username=username)
        new_like.save()
        post.no_of_likes = post.no_of_likes+1
        post.save()
        return redirect('/')
    else:
        like_filter.delete()
        post.no_of_likes = post.no_of_likes-1
        post.save()
        return redirect('/')
    
class AddLike(LoginRequiredMixin, View):
    def post(self,request,pk,*args,**kwargs):
        post = Post.objects.get(pk=pk)
        is_dislike=False
        for dislike in post.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break
        
        if is_dislike:
            post.dislikes.remove(request.user)
        
        is_like = False
        for dislike in post.likes.all():
            if dislike == request.user:
                is_like = True
                break
        if not is_like:
            post.likes.add(request.user)

        if is_like:
            post.likes.remove(request.user)
        
        next = request.POST.get('next','/')
        return redirect('muro')
