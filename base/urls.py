from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index' ),
    path('perfiles/', views.listar_perfiles, name='perfiles_view'),
    path('perfiles/<int:id>', views.recuperar_perfil, name='perfil_view'),
    path('post/<int:id>', views.mostar_post_por_perfil, name='post_view'),
   
] 