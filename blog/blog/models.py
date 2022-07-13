from django.db import models
from django.urls import reverse # allows to reference object by URL template name.

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey( # alows for many-to-one relation. User can be author of many blog posts
        "auth.User", # reference to built in User model.
        on_delete=models.CASCADE, # must be specified for all manay-to-one relationships
    )
    body = models.TextField()

    def __str__(self) -> str:
        return self.title

    # django will automatically use on model if it is available.
    # so after update/create we have redirect to this.
    def get_absolute_url(self): # Tells django how to calculate URL for model object
        # use URL post_detail with pk passed
        return reverse("post_detail", kwargs={"pk": self.pk})