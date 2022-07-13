from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationForm # specify use of built-in form
    success_url = reverse_lazy("login") # why lazy ? for all generic views URLs are not loaded when file is imported
    template_name: str = "registration/signup.html"