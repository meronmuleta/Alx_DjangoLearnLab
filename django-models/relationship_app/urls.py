from django.urls import path
from . import views
from .views import list_books
urlpatterns = [
    path('views/',list_books),
    path('<int:pk>/',views.LibraryDetailView.as_view(),name="library_detail"),
]
