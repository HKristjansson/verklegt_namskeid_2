from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .profile_form import Profile


# class RegistrationForm(UserCreationForm):
#     email = forms.EmailField(required=True)
#
#     class Meta:
#         model = User
#         fields = (
#             'first_name',
#             'last_name',
#             'username',
#             'email',
#             'password1',
#             'password2',
#         )
#
#     def save(self, commit=True):
#         user = super(RegistrationForm, self).save(commit=False)
#         # user.first_name = RegistrationForm.cleaned_data['first_name']
#         # user.last_name = RegistrationForm.cleaned_data['last_name']
#         # user.email = RegistrationForm.cleaned_data['email']
#
#         if commit:
#             user.save()
#
#         return user

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
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
