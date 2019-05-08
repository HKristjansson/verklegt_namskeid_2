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
