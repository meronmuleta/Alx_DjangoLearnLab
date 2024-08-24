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
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),

    ]
