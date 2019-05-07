from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from user.forms.profile_form import ProfileForm
from user.forms.registration_form import RegistrationForm, UserUpdateForm, ProfileUpdateForm
from user.models import Profile
from django.contrib import messages, auth


users = [
    {
        'email': 'some email',
        'id': '1'
    },
    {
        'email': 'some email2',
        'id': '2'
    }
]


# Create your views here.
# maybe to show all users or something
def index(request):
    context = {'users': users}
    return render(request, 'user/index.html', context)


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, '{} Your account has been created! You are now able to log in'.format(username))
            return redirect('profile')
    return render(request, 'user/register.html', {
        'form': RegistrationForm()
    })


# def profile(request):
#     profile = Profile.objects.filter(user=request.user).first()
#     if request.method == 'POST':
#         form = ProfileForm(instance=profile, data=request.POST)
#         if form.is_valid():
#             profile = form.save(commit=False)
#             profile.user = request.user
#             profile.save()
#             return redirect('profile')
#     return render(request, 'user/profile.html', {
#         'form': ProfileForm(instance=profile)
#     })

# TODO: Fix the profile
def profile(request):
    # profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        u_form = UserUpdateForm(instance=profile, data=request.POST)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'user/profile.html', context)


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'user/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('index')
