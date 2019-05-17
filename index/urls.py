from django.urls import path
from .views import CardListView


from . import views

urlpatterns = [
    path('', CardListView.as_view(), name="index"),
    # path('', views.index, name="index"),
    path('about/', views.about, name="about"),
]
