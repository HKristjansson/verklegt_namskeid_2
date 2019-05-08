from django.shortcuts import render


# Create your views here.


def index(request):
    return render(request, 'part/search.html')


def about(request):
    return render(request, 'index/about.html')


