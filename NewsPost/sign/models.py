from django.contrib.auth.forms import UserCreationForm
from django import forms

from news.models import User


class BaseRegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email")

    class Meta:
        model = User
        fields = ("username",
                  "email",
                  "password1",
                  "password2",)
