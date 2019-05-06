from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from apartment.forms.apartment_form import ApartmentAddForm, ApartmentUpdateForm, ApartmentAddPhotoForm
from apartment.models import Apartment, ApartmentImage


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
            for x in range(1, 6):
                x = str(x)
                image = ApartmentImage(image=request.POST['image' + x], apartment=apartment)
                if image.image != '':
                    image.save()
            return redirect('apartment_index')
    else:
        form = ApartmentAddForm()
    return render(request, 'apartment/add_apartment.html', {
        'form': form
    })


@login_required
def remove_apartment(request, id):
    apartment = get_object_or_404(Apartment, pk=id)
    apartment.delete()
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


def apartment_add_photo(request, id):
    instance = get_object_or_404(Apartment, pk=id)
    if request.method == 'POST':
        for x in range(1, 6):
            x = str(x)
            image = ApartmentImage(image=request.POST['image' + x], apartment=instance)
            if image.image != '':
                image.save()
        return redirect('apartment_details', id=id)
    else:
        form = ApartmentAddPhotoForm(instance=instance)
    return render(request, 'apartment/apartment_add_photo.html', {
        'form': form,
        'id': id
    })

