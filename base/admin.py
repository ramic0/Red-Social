from django.contrib import admin
from .models import Perfil, Post, FollowersCount

admin.site.register(Perfil)
admin.site.register(Post)
admin.site.register(FollowersCount)