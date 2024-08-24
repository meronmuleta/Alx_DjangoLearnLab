from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from .models import Library
from typing import Any
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'relationship_app/register.html'
    success_url = reverse_lazy('profile')  

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class Login(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'relationship_app/login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')  
        return render(request, 'relationship_app/login.html', {'form': form})


class Logout(View):
    def get(self, request):
        logout(request)
        return render(request, 'relationship_app/logout.html')

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

