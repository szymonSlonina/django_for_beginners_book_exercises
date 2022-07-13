from django.views.generic import ListView

from .models import Post

# Create your views here.
# ListView automatically returns context variable <model>_list, that we can loop over via built-in for template tag.
class HomePageView(ListView):
    model = Post # import model
    template_name: str = "home.html" # import template