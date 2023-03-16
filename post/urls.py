from django.urls import path
from . import views
from .views import AddLike

urlpatterns = [
    path('crear/post/', views.crearPost, name='crearPost'),
    path('ver/', views.ver_post, name='ver_post' ),
    path('detalle/<int:post_id>', views.post_detail, name='post_detail'),
    path('detalle/<int:post_id>/delete', views.post_delete, name='post_delete'),
    path('like-post/<int:post_id>', views.like_post, name='like_post'),
    path('<int:pk>/like', AddLike.as_view(), name='like_post'),
]