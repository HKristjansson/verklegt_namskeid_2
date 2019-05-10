from django.shortcuts import render, get_object_or_404
from seller.models import Seller, SellerImage
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from seller.forms.seller_form import SellerAddForm, SellerUpdateForm

# Create your views here.
#def index(request):
#    context = {'sellers': Seller.objects.all().order_by('name')
#               }
#    return render(request, 'seller/seller_index.html', context)

def index(request):
    context = {'sellers': Seller.objects.all().order_by('name')
               }
    return render(request, 'seller/seller_index.html', context)

def get_seller_by_id(request, id):
    return render(request, 'seller/seller_details.html', {
        'seller': get_object_or_404(Seller, pk=id)
    })

@login_required
def add_seller(request):
    if request.method == 'POST':
        form = SellerAddForm(data=request.POST)
        if form.is_valid():
            seller = form.save()
            seller_image = SellerImage(image=request.POST['image'], seller=seller)
            seller_image.save()
            return redirect('seller_index')
    else:
        form = SellerAddForm()
    return render(request, 'seller/add_seller.html', {
        'form': form
    })

@login_required
def update_seller(request, id):
    instance = get_object_or_404(Seller, pk=id)
    if request.method == 'POST':
        form = SellerUpdateForm(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('seller_details', id=id)
    else:
        form = SellerUpdateForm(instance=instance)
    return render(request, 'seller/update_seller.html', {
        'form': form,
        'id': id
    })

@login_required
def remove_seller(request, id):
    seller = get_object_or_404(Seller,pk=id)
    seller.delete()
    seller['disabled'] == 1
    #seller['available'] == 0
    return redirect('seller_index')
