from django.urls import path
from .views import RegisterView, LoginView, UserFollowView, UserUnfollowView, UserListView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:user_id>/follow/', UserFollowView.as_view(), name='follow-user'),
    path('users/<int:user_id>/unfollow/', UserUnfollowView.as_view(), name='unfollow-user'),
]
