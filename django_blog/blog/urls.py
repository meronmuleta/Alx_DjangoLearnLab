from django.urls import path
from django.contrib.auth import views as auth_views
from .views import RegisterView, profile_view, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, CommentCreateView, CommentUpdateView, CommentDeleteView


urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name='blog/login.html'),name='login'),
    path('logout',auth_views.LogoutView.as_view(),name='logout'),
    path('register/',RegisterView.as_view(),name='register'),
    path('profile/',profile_view,name='profile'),
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/comment/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]