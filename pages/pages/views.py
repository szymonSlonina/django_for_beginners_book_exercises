from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
# class based views
# real power in extending them.
class HomePageView(TemplateView):
    template_name = "home.html"

class AboutPageView(TemplateView):
    template_name = "about.html"