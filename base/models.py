from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(max_length=100, blank=False, null=False)
    bio = models.TextField()
    avatar = models.ImageField(default='image/usuario.png')

    def __str__(self):
        return self.usernames

class Post(models.Model):
    user = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    time = models.DateTimeField(default=timezone.now)
    content = models.TextField(max_length=500)

    def __str__(self):
        return self.content

