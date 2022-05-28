from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from . import models
#authentication start
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
#authentication start
#registration start
from django.shortcuts import render, redirect
from .forms import RegisterForm
#registration end
#authentication start here     
class BookCreateView(LoginRequiredMixin, CreateView):
    model = models.Book
    fields = "__all__"
    success_url = "/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)	
#authentication end here         

class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Book
    fields = "__all__"
    success_url = "/"  

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)	
        
class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Book
    success_url = "/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
#registration start
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect("/")
    else:
        form = RegisterForm()
        
    return render(response, "registration/register.html", {"form":form})

class BookListView(ListView):
    model = models.Book

class BookDetailView(DetailView):
    model = models.Book
#registration end    
