from django.urls import path
from django.contrib.auth import views as auth_views
from .views import RegisterView, profile_view

urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name='blog/login.html'),name='login'),
    path('logout',auth_views.LogoutView.as_view(),name='logout'),
    path('register/',RegisterView.as_view(),name='register'),
    path('profile/',profile_view,name='profile'),
]