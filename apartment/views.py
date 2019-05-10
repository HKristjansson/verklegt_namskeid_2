from functools import reduce
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from apartment.forms.apartment_form import ApartmentAddForm, ApartmentUpdateForm
from apartment.models import Apartment, ApartmentImage
from user.models import User
import operator


def get_apartment_by_id(request, id):
    return render(request, 'apartment/apartment_details.html', {
        'apartment': get_object_or_404(Apartment, pk=id)
    })


@login_required
def add_apartment(request):
    if request.method == 'POST':
        form = ApartmentAddForm(data=request.POST)
        if form.is_valid():
            apartment = form.save()
            apartment_image = ApartmentImage(image=request.POST['image'], apartment=apartment)
            apartment_image.save()
            return redirect('apartment_index')
    else:
        form = ApartmentAddForm()
    return render(request, 'apartment/add_apartment.html', {
        'form': form
    })

@login_required
def remove_apartment(request, id):
    apartment = get_object_or_404(Apartment, pk=id)
    apartment['available'] == 0
    apartment.save()
    return redirect('apartment_index')

@login_required
def update_apartment(request, id):
    instance = get_object_or_404(Apartment, pk=id)
    if request.method == 'POST':
        form = ApartmentUpdateForm(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('apartment_details', id=id)
    else:
        form = ApartmentUpdateForm(instance=instance)
    return render(request, 'apartment/update_apartment.html', {
        'form': form,
        'id': id
    })

def index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        apartments = [{
            'id': x.id,
            'address': x.address,
            'description': x.description,
            'firstImage': x.apartmentimage_set.first().image
        } for x in Apartment.objects.filter(address__icontains=search_filter)
        ]
        return JsonResponse({'data': apartments})
    context = {'apartments': Apartment.objects.all().order_by('address')}
    return render(request, 'apartment/apartment_index.html', context)


def search_apartment(request):
    if 'search_filter' in request.GET:  # set a hidden field (search_filter) so you know that you need to perform a search
        search_params = request.GET.dict()
        search_params.pop("search_filter")
        q_list = [Q(("{}__icontains".format(param), search_params[param])) for param in search_params if
                  search_params[param] is not None]

        queryset = Apartment.objects.filter(reduce(operator.and_, q_list))
        apartments = [{
            'id': x.id,
            'address': x.address,
            'zip': x.zip,
            'description': x.description,
            'price': x.price,
            'category': str(x.category),
            'firstImage': x.apartmentimage_set.first().image
        } for x in queryset
        ]
        return JsonResponse({'data': apartments})
    context = {'apartments': Apartment.objects.all().order_by('price')}
    print(context)
    return render(request, 'part/search_no_base.html', context)


