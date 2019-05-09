from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="sellerIndex"),
    path('<int:id>', views.get_seller_by_id, name="seller_details"),
    path('create_seller',views.create_seller,name="create_seller")
    #path('delete_seller')
]
