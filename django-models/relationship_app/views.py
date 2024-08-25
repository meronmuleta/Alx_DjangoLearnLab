from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from .models import Library
from typing import Any
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import user_passes_test

class register(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = "relationship_app/register.html"

    def get_form(self, form_class=None):
        form = UserCreationForm()
        return super().get_form(form_class or form)



def list_books(request):
    list_books= Book.objects.all()
    context = {'books':list_books}
    return render(request,'relationship_app/list_books.html',context)


class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()
        return context


def Admin(user):
    return user.userprofile.role == 'Admin'

def Librarian(user):
    return user.userprofile.role == 'Librarian'

def Member(user):
    return user.userprofile.role == 'Member'

@user_passes_test(Admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(Librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(Member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
