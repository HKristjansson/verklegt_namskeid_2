from functools import reduce
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from apartment.forms.apartment_form import ApartmentAddForm, ApartmentUpdateForm, ApartmentBuyForm
from apartment.models import Apartment, ApartmentImage, ZIP, ApartmentCategory
from user.forms.registration_form import Payment
import datetime
import operator


def get_apartment_by_id(request, id):
    apartments = Apartment.objects.all()
    building_types = ApartmentCategory.objects.all()
    zip_code = ZIP.objects.all().values("zip", "city")
    context = {'apartments': apartments, 'building_types': building_types, 'zip': zip_code,
               'apartment': get_object_or_404(Apartment, pk=id)}
    return render(
        request, 'apartment/apartment_details.html', context
    )


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
    apartment.sold = True
    apartment.save()
    return redirect('apartment_index')


def buy_apartment_step_one(request, id):
    instance = get_object_or_404(Apartment, pk=id)
    current_user = request.user
    if request.method == 'POST':
        print(current_user.id)
        apartment_form = ApartmentBuyForm(data=request.POST, instance=instance)
        credit_card_form = Payment(data=request.POST)
        if apartment_form.is_valid() and credit_card_form.is_valid():
            instance.sold = True
            apartment_form.save()
            #credit_card_form.date = datetime.date.today() # gúgglum hvernig við fáum NOW í þessu

            credit_card_form.save()
            return redirect('apartment_details', id=id)
    else:
        apartment_form = ApartmentBuyForm(instance=instance)
        credit_card_form = Payment(data=request.POST, instance=instance)
    return render(request, 'apartment/buy_apartment_step_one.html', {
        'form': apartment_form,
        'id': id,
        'cardholder': request.user,
        'credit_card': credit_card_form
    })


@login_required
def update_apartment(request, id):
    instance = get_object_or_404(Apartment, pk=id)
    if request.method == 'POST':
        form = ApartmentUpdateForm(data=request.POST, instance=instance)
        if form.is_valid():
            ApartmentImage.objects.filter(pk=id).update(image=request.POST['image'])
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
        print(search_filter)
        apartments = [{
            'id': x.id,
            'address': x.address,
            'description': x.description,
            'firstImage': x.apartmentimage_set.first().image
        } for x in Apartment.objects.filter(address__icontains=search_filter)
        ]
        return JsonResponse({'data': apartments})
    apartments = Apartment.objects.all()
    building_types = ApartmentCategory.objects.all()
    zip_code = ZIP.objects.all().values("zip", "city")
    context = {'apartments': apartments, 'building_types': building_types, 'zip': zip_code}
    return render(request, 'apartment/apartment_index.html', context)


def search_apartment(request):
    if 'search_filter' in request.GET:
        search_params = request.GET.dict()
        search_params.pop('search_filter')

        price_from = search_params.pop('price_from', None)
        price_to = search_params.pop('price_to', None)
        q_list = [
            Q(('{}__icontains'.format(k), v))
            for k, v in search_params.items()
            if v is not None
        ]
        if int(price_to) > 0:
            price = {'price__gte': price_from, 'price__lte': price_to}
        else:
            price = {'price__gte': price_from, 'price__gt': price_to}
        q_list.append(Q(**{k: v for k, v in price.items() if v is not None}))
        print(q_list)
        queryset = Apartment.objects.filter(reduce(operator.and_, q_list))
        apartments = [{
            'id': x.id,
            'address': x.address,
            'zip': str(x.zip),
            'description': x.description,
            'price': x.price,
            'category': str(x.category),
            'firstImage': x.apartmentimage_set.first().image
        } for x in queryset
        ]
        return JsonResponse({'data': apartments})
    apartments = Apartment.objects.all()
    building_types = ApartmentCategory.objects.all()
    zip_code = ZIP.objects.all().values("zip", "city")
    context = {'apartments': apartments, 'building_types': building_types, 'zip': zip_code}
    return render(request, 'apartment/apartment_index.html', context)


def sold_apartments(request):
    apartments = Apartment.objects.all()
    building_types = ApartmentCategory.objects.all()
    zip_code = ZIP.objects.all()
    context = {'apartments': apartments, 'building_types': building_types, 'zip': zip_code}
    return render(request, 'apartment/sold_apartments.html', context)
