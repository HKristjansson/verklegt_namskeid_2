from django import forms
from django.forms import ModelForm, widgets
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .profile_form import Profile
from user.models import Sale
import datetime


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name',
                  'last_name',
                  'username',
                  'email',
                  'password1',
                  'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name',
                  'last_name',
                  'username',
                  'email'
                ]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
                  'address',
                  'phone',
                  'image'
                  ]


class Payment(ModelForm):
    user = forms.Select()
    apartment = forms.Select()
    date = forms.DateTimeField()

    class Meta:
        model = Sale
        exclude = []
        widgets = {
            'card_num_1': widgets.NumberInput(attrs={'class': 'form-control-row', 'max_length': 4}),
            'card_num_2': widgets.NumberInput(attrs={'class': 'form-control-row', 'max_length': 4}),
            'card_num_3': widgets.NumberInput(attrs={'class': 'form-control-row', 'max_length': 4}),
            'card_num_4': widgets.NumberInput(attrs={'class': 'form-control-row', 'max_length': 4}),
            'cvc': widgets.NumberInput(attrs={'class': 'form-control-row', 'max_length': 3}),
            'expire': widgets.DateInput(attrs={'class': 'form-control-row'})
        }

