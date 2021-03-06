from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from user.forms.registration_form import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, Payment
from django.contrib import messages, auth
from django.http import HttpResponseForbidden
from django.contrib import messages


def index(request):
    return HttpResponseForbidden()


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, '{}, Your account has been created! You are now able to log in'.format(username))
            return redirect('index')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
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
        'p_form': p_form,
    }
    if request.user.is_authenticated:
        return render(request, 'user/profile.html', context)
    else:
        return HttpResponseForbidden()


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, f'You are now logged in')
            return redirect('index')
        else:
            messages.error(request, f'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, f'You are now logged out')
        return redirect('index')

