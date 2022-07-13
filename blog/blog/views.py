from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Post

# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name: str = "home.html"

# detail view provides us with context object called object
# or lowercased name of model
class BlogDetailView(DetailView):
    model = Post
    template_name: str = "post_detail.html"

class BlogCreateView(CreateView):
    model = Post
    template_name: str = "post_new.html"
    fields = ["title", "author", "body"] # aditionally we specify fields we want to expose

class BlogUpdateView(UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields = ["title", "body"]

class BlogDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home") # redirect after deletion to homepage.
    # reverse lazy won't execute until view has finished deleting.