from django.shortcuts import render
from apartment.models import Apartment, ApartmentCategory, ZIP, ApartmentSearch
from django.views.generic import ListView
from django.shortcuts import render_to_response
from django.template import RequestContext


# Create your views here.
class CardListView(ListView):
    model = Apartment
    template_name = 'index/index.html'
    context_object_name = 'apartments'
    ordering = ['price']
    paginate_by = 8
    limit = 30

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        userid = self.request.user.id
        search_history = ApartmentSearch.objects.all().order_by('-date').filter(user=userid)[:5]
        building_types = ApartmentCategory.objects.all()
        zip_code = ZIP.objects.all()
        context['zip_code'] = zip_code
        context['search_history'] = search_history
        context['building_types'] = building_types
        return context

    def get_queryset(self):
        return super().get_queryset().filter(sold=False)[:self.limit]


def about(request):
    return render(request, 'index/about.html')


def handler404(request, *args, **argv):
    response = render_to_response('errors/404.html')
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    response = render_to_response('errors/500.html')
    response.status_code = 500
    return response
