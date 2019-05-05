from django.shortcuts import render

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
