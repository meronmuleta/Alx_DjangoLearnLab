from django.urls import path
from .views import RegisterView, LoginView, UserFollowView, UserUnfollowView, UserListView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/follow/<int:user_id>/', UserFollowView.as_view(), name='follow-user'),
    path('users/unfollow/<int:user_id>/', UserUnfollowView.as_view(), name='unfollow-user'),


]
