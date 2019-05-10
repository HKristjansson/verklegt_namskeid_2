from django.http import JsonResponse
from django.shortcuts import render
from apartment.models import Apartment, ApartmentCategory

# Create your views here.


def index(request):
    apartments = Apartment.objects.all().order_by('-created')
    building_types = ApartmentCategory.objects.all()
    context = {'apartments': apartments, 'building_types': building_types}
    return render(request, 'index/index.html', context)


def about(request):
    return render(request, 'index/about.html')


