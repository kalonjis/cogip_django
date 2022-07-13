from django.contrib.auth.forms import UserCreationForm

from office.models import CustomUser


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username",)
