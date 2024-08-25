from django.urls import path
from . import views
from .views import list_books
from .views import SignUpView, Login, Logout
from .views import AdminView, LibrarianView, MemberView

urlpatterns = [
    path('views/',list_books),
    path('<int:pk>/',views.LibraryDetailView.as_view(),name="library_detail"),
    path('register/', views.register.as_view(), name="register"),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name="login"),
    path('logout/',LogoutView.as_view(template_name='relationship_app/logout.html'), name="logout"),
    path('admin/', AdminView, name='Admin'),
    path('librarian/', LibrarianView, name='Librarian'),
    path('member/', MemberView, name='Member'),

    ]
