from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="sellerIndex"),
    path('<int:id>', views.get_seller_by_id, name="seller_details")
]
