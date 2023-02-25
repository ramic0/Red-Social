from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index' ),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('perfil/', views.perfil, name='perfil'),
    #path('perfil/<str:username>', views.perfil, name='perfil'),
]