from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.muro, name='muro' ),
    path('signup/', views.signup, name='signup' ),
    path('login/', LoginView.as_view(), name='login' ),
    path('perfil/', views.ver_perfil, name='ver_perfil' ),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('logout/', views.signout, name='logout' ),
    path('signin/', views.signin, name='signin' ),
    path('settings/', views.settings, name='settings' ),
    path('upload', views.upload, name='upload'),
    path('follow/<str:username>/', views.follow, name='follow'),
    path('unfollow/<str:username>/', views.unfollow, name='unfollow'),
]