from functools import reduce
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from apartment.forms.apartment_form import ApartmentAddForm, ApartmentUpdateForm, ApartmentBuyForm
from apartment.models import Apartment, ApartmentImage, ZIP, ApartmentCategory, ApartmentSearch
from user.forms.registration_form import Payment
from django.utils import timezone
import operator
from django.views.generic import ListView


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


@login_required
def buy_apartment_step_one(request, id):
    instance = get_object_or_404(Apartment, pk=id)
    if request.method == 'POST':
        apartment_form = ApartmentBuyForm(data=request.POST, instance=instance)
        credit_card_form = Payment(data=request.POST)
        if apartment_form.is_valid() and credit_card_form.is_valid():
            apartment_form.instance.buyer = request.user
            apartment_form.save()
            credit_card_form.instance.apartment = instance
            credit_card_form.instance.cardholder = request.user
            credit_card_form.instance.date = timezone.now()
            credit_card_form.save()
            crid = credit_card_form.id

            return redirect('buy_apartment_step_two', id=crid.id)
    else:
        apartment_form = ApartmentBuyForm(instance=instance)
        credit_card_form = Payment(data=request.POST, instance=instance)
    return render(request, 'apartment/buy_apartment_step_one.html', {
        'form': apartment_form,
        'id': id,
        'cardholder': request.user,
        'credit_card': credit_card_form
    })


def buy_apartment_step_two(request, id):
    instance = get_object_or_404(Apartment, pk=id)
    if request.method == 'POST':
        credit_card_form = Payment(data=request.POST)
        apartment_form = ApartmentBuyForm(data=request.POST)
        context = {
            'id': id,
            'apartment': apartment_form,
            'purchaseinfo': credit_card_form
        }
        return render(request, 'apartment/buy_apartment_step_two.html', context)

    return render(
        request, 'apartment/buy_apartment_step_two.html', {

        })


def buy_apartment_step_three(request, id):

    Apartment.objects.filter(pk=id).update(sold=True)
    return render(request, 'apartment/buy_apartment_step_three.html')


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
    apartments = Apartment.objects.all()
    building_types = ApartmentCategory.objects.all()
    zip_code = ZIP.objects.all().values("zip", "city")
    context = {'apartments': apartments, 'building_types': building_types, 'zip': zip_code}
    return render(request, 'apartment/apartment_index.html', context)


def search_apartment(request):
    if 'search_history' in request.GET:
        new_search_params = {}
        search_hist = request.GET.dict()
        id = int(search_hist.get('search_history'))
        search_params = get_object_or_404(ApartmentSearch, pk=id)
        price_from = search_params.price_from
        new_search_params['address'] = search_params.address
        new_search_params['zip__zip'] = search_params.zip
        new_search_params['number'] = search_params.number
        new_search_params['category__name'] = search_params.category
        price_from = search_params.price_from
        price_to = search_params.price_to
        size_from = search_params.size_from
        size_to = search_params.size_to
        rooms_from = search_params.size_from
        rooms_to = search_params.rooms_to
        order_by = str(search_params.pop('order_by', None))
        q_list = [
            Q(('{}__icontains'.format(k), v))
            for k, v in new_search_params.items()
            if v is not None
        ]
        if int(price_to) > 0:
            price = {'price__gte': price_from, 'price__lte': price_to}
        else:
            price = {'price__gte': price_from, 'price__gt': price_to}
        if int(size_to) > 0:
            size = {'size__gte': size_from, 'size__lte': size_to}
        else:
            size = {'size__gte': size_from, 'size__gt': size_to}
        if int(rooms_to) > 0:
            rooms = {'rooms__gte': rooms_from, 'rooms__lte': rooms_to}
        else:
            rooms = {'rooms__gte': rooms_from, 'rooms__gt': rooms_to}
        q_list.append(Q(**{k: v for k, v in price.items() if v is not None}))
        q_list.append(Q(**{k: v for k, v in size.items() if v is not None}))
        q_list.append(Q(**{k: v for k, v in rooms.items() if v is not None}))
        queryset = Apartment.objects.filter(reduce(operator.and_, q_list)).order_by(order_by)
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

    elif 'search_filter' in request.GET:
        search_params = request.GET.dict()
        search_params.pop('search_filter')
        search_save = dict(search_params)
        price_from = int(search_params.pop('price_from', None))
        price_to = int(search_params.pop('price_to', None))
        size_from = int(search_params.pop('size_from', None))
        size_to = int(search_params.pop('size_to', None))
        rooms_from = int(search_params.pop('rooms_from', None))
        rooms_to = int(search_params.pop('rooms_to', None))
        order_by = str(search_params.pop('order_by', None))
        print(order_by)
        q_list = [
            Q(('{}__icontains'.format(k), v))
            for k, v in search_params.items()
            if v is not None
        ]
        if int(price_to) > 0:
            price = {'price__gte': price_from, 'price__lte': price_to}
        else:
            price = {'price__gte': price_from, 'price__gt': price_to}
        if int(size_to) > 0:
            size = {'size__gte': size_from, 'size__lte': size_to}
        else:
            size = {'size__gte': size_from, 'size__gt': size_to}
        if int(rooms_to) > 0:
            rooms = {'rooms__gte': rooms_from, 'rooms__lte': rooms_to}
        else:
            rooms = {'rooms__gte': rooms_from, 'rooms__gt': rooms_to}
        q_list.append(Q(**{k: v for k, v in price.items() if v is not None}))
        q_list.append(Q(**{k: v for k, v in size.items() if v is not None}))
        q_list.append(Q(**{k: v for k, v in rooms.items() if v is not None}))
        queryset = Apartment.objects.filter(reduce(operator.and_, q_list)).order_by(order_by)
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

        if request.user.is_authenticated:
            category = search_save.pop('category__name', None)
            new_zip = search_save.pop('zip__zip', None)
            instance = ApartmentSearch(**search_save)
            instance.user = request.user
            instance.date = timezone.now()
            instance.category = category
            instance.zip = new_zip
            instance.save()
        return JsonResponse({'data': apartments})
    apartments = Apartment.objects.all()
    building_types = ApartmentCategory.objects.all()
    zip_code = ZIP.objects.all().values("zip", "city")
    context = {'apartments': apartments, 'building_types': building_types, 'zip': zip_code}
    return render(request, 'apartment/apartment_index.html', context)


class ApartmentListView(ListView):
    model = Apartment
    template_name = 'apartment/apartment_index.html'
    context_object_name = 'apartments'
    ordering = ['-created']
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


def sold_apartments(request):
    apartments = Apartment.objects.all()
    building_types = ApartmentCategory.objects.all()
    zip_code = ZIP.objects.all()
    context = {'apartments': apartments, 'building_types': building_types, 'zip': zip_code}
    return render(request, 'apartment/sold_apartments.html', context)
