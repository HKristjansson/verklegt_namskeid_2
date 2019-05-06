from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

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
def index(request):
    context = {'users': users}
    return render(request, 'user/index.html', context)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'user/register.html', {
        'form': UserCreationForm()
    })
