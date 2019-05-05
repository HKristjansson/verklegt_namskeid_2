from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="apartment_index"),
    path('<int:id>', views.get_apartment_by_id, name="apartment_details"),
    path('add_apartment', views.add_apartment, name="add_apartment"),
    path('remove_apartment/<int:id>', views.remove_apartment, name="remove_apartment"),
    path('update_apartment/<int:id>', views.update_apartment, name="update_apartment")

]
