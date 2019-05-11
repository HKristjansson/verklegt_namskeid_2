from django.http import JsonResponse
from django.shortcuts import render
from apartment.models import Apartment, ApartmentCategory, ZIP

# Create your views here.


def index(request):
    apartments = Apartment.objects.all().order_by('-created')
    building_types = ApartmentCategory.objects.all()
    zip_code = ZIP.objects.all()
    context = {'apartments': apartments, 'building_types': building_types, 'zip': zip_code}
    return render(request, 'index/index.html', context)


def about(request):
    return render(request, 'index/about.html')


