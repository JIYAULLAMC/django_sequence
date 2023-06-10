from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        # username password1 and password2 will come from UserCreationForm
        fields = ["username", "first_name", "last_name", "email"]

        # changing the label
        labels = {'email' : "Enter Email Here !( label changed)"}