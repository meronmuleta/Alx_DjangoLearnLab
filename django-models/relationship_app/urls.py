from django.urls import path
from . import views

urlpatterns = [
    path('views/',views.BookList),
    path('<int:pk>/',views.LibraryDetailView.as_view(),name="library_detail"),
]
