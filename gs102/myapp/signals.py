

# this will demonstrate how to remove the page along with user who have created it
# on_delete = models.CASCAD  in user model will help to remove the user along with the page associated with it
# this also you can do by using the actions 

# using signals we can do as below

from myapp.models import Page
from django.contrib.auth.models import User
from django.db.models.signals import post_delete
from django.dispatch import receiver

@receiver(post_delete, sender=Page)
def delete_related_user(sender, instance, **kwargs):
    print("-----------------------------------", sender.__dict__)
    print("-----------------------------------", instance.__dict__)
    print("-----------------------------------", {**kwargs})

    instance.user.delete()