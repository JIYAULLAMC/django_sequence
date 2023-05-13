from django.db import models
from django.contrib.auth. models import User

# Create your models here.


class Page(models.Model):
    # cascad used when the user removed the page respective to same user also get removed
    # user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    # protect help not to delete the user when any pages are associated with the user
    user = models.OneToOneField(User, on_delete=models.PROTECT, primary_key=True)
    page_name = models.CharField(max_length=40)
    page_desc = models.CharField(max_length=100)
