from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        # username password1 and password2 will come from UserCreationForm
        fields = ["username", "first_name", "last_name", "email"]

        # changing the label
        labels = {'email' : "Enter Email Here !( label changed)"}


# for normal user
class UserEditForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]
        label = { "email" : "Email"}


# for special admin user

class AdminUserEditForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = "__all__"
        label = { "email" : "Email"}