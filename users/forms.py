from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from .models import payment

class signup(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model = User
        fields = ('username','email','password1','password2')
class pay(ModelForm):
    class Meta:
        model = payment
        fields = "__all__"