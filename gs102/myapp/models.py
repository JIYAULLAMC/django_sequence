from django.db import models
from django.contrib.auth. models import User

# Create your models here.


class Page(models.Model):
    # limit_choices_to help to create the pages for them only what it include as key in its dictionary 
    # limit_choices_to help to create page and for some like "is_staff" and it will restrict for creating the page
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, limit_choices_to={'is_staff': True})
    page_name = models.CharField(max_length=40)
    page_desc = models.CharField(max_length=100)
