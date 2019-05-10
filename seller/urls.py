from django.urls import path

from . import views

urlpatterns = [
    path('', views.index,  name="seller_index"),
    path('<int:id>', views.get_seller_by_id, name="seller_details"),
    path('add_seller', views.add_seller, name="add_seller"),
    path('update_seller/<int:id>', views.update_seller, name="update_seller"),
    path('remove_seller/<int:id>', views.remove_seller, name="remove_seller"),

]
