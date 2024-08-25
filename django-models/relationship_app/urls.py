from django.urls import path
from . import views
from .views import list_books
from .views import SignUpView, Login, Logout
from .views import admin_view, librarian_view, member_view

urlpatterns = [
    path('views/',list_books),
    path('<int:pk>/',views.LibraryDetailView.as_view(),name="library_detail"),
    path('register/', views.register.as_view(), name="register"),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name="login"),
    path('logout/',LogoutView.as_view(template_name='relationship_app/logout.html'), name="logout"),
    path('admin/', admin_view, name='Admin'),
    path('librarian/', librarian_view, name='Librarian'),
    path('member/', member_view, name='Member'),
    path('add_book/', BookCreateView.as_view(), name='book_add'),
    path('edit_book/', BookUpdateView.as_view(), name='book_edit'),
    path('delete_book/', BookDeleteView.as_view(), name='book_delete'),

    ]
