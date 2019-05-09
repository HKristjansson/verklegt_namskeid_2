from django.shortcuts import render, get_object_or_404
from seller.models import Seller


# Create your views here.


def index(request):
    context = {'sellers': Seller.objects.all().order_by('name')

               }
    return render(request, 'seller/seller_index.html', context)

def get_seller_by_id(request, id):
    return render(request, 'seller/seller_details.html', {
        'seller': get_object_or_404(Seller, pk=id)
    })


def create_seller(request):
    if request.method == 'POST':
        form = SellerCreateForm(data=request.POST)
        if form.is_valid():
            seller = form.save()
            seller_image = SellerImage(image=request.POST['image'], seller=seller)
            seller_image.save()
            return redirect('seller_index')
    else:
        form = SellerCreateForm()
    return render(request, 'seller/add_seller.html', {
        'form': form
    })

def delete_seller(request, id):
    seller = get_object_or_404(seller,pk=id)
    seller.delete()
    return redirect('seller_index')
