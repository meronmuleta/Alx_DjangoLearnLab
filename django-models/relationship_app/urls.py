from django.urls import path
from . import views
from .views import list_books
from .views import SignUpView, Login, Logout
urlpatterns = [
    path('views/',list_books),
    path('<int:pk>/',views.LibraryDetailView.as_view(),name="library_detail"),
    path('register/', SignUpView.as_view(), name="register"),
    path('login/', Login.as_view(), name="login"),
    path('logout/',Logout.as_view(), name="logout"),
]
