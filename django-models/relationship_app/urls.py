from django.urls import path
from . import views
from .views import list_books
from django.contrib.auth.views import LoginView, LogoutView
from .views import SignUpView
urlpatterns = [
    path('views/',list_books),
    path('<int:pk>/',views.LibraryDetailView.as_view(),name="library_detail"),
    path('register/', SignUpView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/',LogoutView.as_view(), name="logout"),
]
