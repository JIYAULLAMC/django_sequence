from django.db import models
from django.contrib.auth. models import User

# Create your models here.


class Page(models.Model):
    # limit_choices_to help to create the pages for them only what it include as key in its dictionary 
    # limit_choices_to help to create page and for some like "is_staff" and it will restrict for creating the page
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, limit_choices_to={'is_staff': True})
    page_name = models.CharField(max_length=40)
    page_desc = models.CharField(max_length=100)




class Post(models.Model):
    # ondelete = models.CASCAD 
    # case when removing the user(parent) - post also get removed
    # case when removing the post- only post will remove
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # ondelete = models.PROTECT
    # case when removing the user(parent) - it will not let to remove the user untill you remove all the post
    #  case when removing the post- only post will remove
    # user = models.ForeignKey(User, on_delete=models.PROTECT)
    
    
    # ondelete = models.SET_NULL
    # case when removing the user(parent) - post will not removed insted user set to null
    # case when removing the post- only post will remove
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
