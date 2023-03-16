from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from accounts.models import Relationship

class Perfil(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=False, null=False)
    apellido = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(max_length=100, blank=False, null=False)
    bio = models.TextField()
    avatar = models.ImageField(default='usuario.png')

    def __str__(self):
        return self.name
    
    def following(self):
        user_ids = Relationship.objcts.filter(from_user=self.user)\
                                .values_list('to_user_id', flat=True)
        return User.objects.filter(id__in=user_ids)
    
    def followers(self):
        user_ids = Relationship.objcts.filter(to_user=self.user)\
                                .values_list('from_user_id', flat=True)
        return User.objects.filter(id__in=user_ids)

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='posts')
    image = models.ImageField(upload_to='post_images')
    caption = models.TextField()
    time = models.DateTimeField(default=timezone.now)
    content = models.TextField(max_length=500)
    likes = models.ManyToManyField(User, blank=True, related_name='likes')

    def __str__(self):
        return self.content


