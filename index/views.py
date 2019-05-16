from django.shortcuts import render
from apartment.models import Apartment, ApartmentCategory, ZIP, ApartmentSearch
from django.core.paginator import Paginator
from django.views.generic import ListView


# Create your views here.


class CardListView(ListView):
    model = Apartment
    template_name = 'index/index.html'
    context_object_name = 'apartments'
    ordering = ['created']
    paginate_by = 10
    limit = 10

    # def get_queryset(self):
    #     return Apartment.objects.all()[:self.limit]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context['paginator']
        page_numbers_range = 10  # Display 5 page numbers
        max_index = len(paginator.page_range)

        page = self.request.GET.get('page')
        current_page = int(page) if page else 1

        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range
        if end_index >= max_index:
            end_index = max_index

        userid = self.request.user.id
        search_history = ApartmentSearch.objects.all().order_by('-date').filter(user=userid)[:5]
        page_range = paginator.page_range[start_index:end_index]
        apartments = Apartment.objects.all()[:self.limit]
        building_types = ApartmentCategory.objects.all()
        zip_code = ZIP.objects.all()
        context['apartments'] = apartments
        context['zip_code'] = zip_code
        context['building_types'] = building_types
        context['page_range'] = page_range
        context['search_history'] = search_history
        return context


# def index(request):
#     apartment_list = Apartment.objects.all().order_by('-created')
#     building_types = ApartmentCategory.objects.all()
#     zip_code = ZIP.objects.all()
#     paginator = Paginator(apartment_list, 4)
#     page = request.POST.get('page', 'Default')
#     apartments = paginator.get_page(page)
#     context = {'apartments': apartments, 'building_types': building_types, 'zip': zip_code}
#     return render(request, 'index/index.html', context)


def about(request):
    return render(request, 'index/about.html')
