from django.shortcuts import render
from apartment.models import Apartment, ApartmentCategory, ZIP
from django.core.paginator import Paginator
from django.views.generic import ListView

# Create your views here.


class CardListView(ListView):
    model = Apartment
    template_name = 'index/index.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'apartments'
    ordering = ['-created']
    paginate_by = 8


def index(request):
    apartment_list = Apartment.objects.all().order_by('-created')
    building_types = ApartmentCategory.objects.all()
    zip_code = ZIP.objects.all()
    paginator = Paginator(apartment_list, 4)
    page = request.POST.get('page', 'Default')
    apartments = paginator.get_page(page)
    context = {'apartments': apartments, 'building_types': building_types, 'zip': zip_code}
    return render(request, 'index/index.html', context)


def about(request):
    return render(request, 'index/about.html')


