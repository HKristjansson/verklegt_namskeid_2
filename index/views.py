from django.http import JsonResponse
from django.shortcuts import render
from apartment.models import Apartment

# Create your views here.



def index(request):
    # apartments = Apartment.objects.all()
    context = {'apartments': Apartment.objects.all().order_by('-created')}
    return render(request, 'index/index.html', context)


def about(request):
    return render(request, 'index/about.html')


