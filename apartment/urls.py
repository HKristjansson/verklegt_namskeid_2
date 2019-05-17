from django.urls import path
from .views import ApartmentListView

from . import views

urlpatterns = [
    path('', ApartmentListView.as_view(), name="apartment_index"),
    path('<int:id>', views.get_apartment_by_id, name="apartment_details"),
    path('add_apartment/', views.add_apartment, name="add_apartment"),
    path('remove_apartment/<int:id>', views.remove_apartment, name="remove_apartment"),
    path('update_apartment/<int:id>', views.update_apartment, name="update_apartment"),
    path('search_apartment/', views.search_apartment, name="search_apartment"),
    path('buy_apartment_step_one/<int:id>', views.buy_apartment_step_one, name='buy_apartment_step_one'),
    path('buy_apartment_step_two/<int:id>', views.buy_apartment_step_two, name='buy_apartment_step_two'),
    path('buy_apartment_step_three/<int:id>', views.buy_apartment_step_three, name='buy_apartment_step_three'),
    path('sold_apartments/', views.sold_apartments, name="sold_apartments"),
]

