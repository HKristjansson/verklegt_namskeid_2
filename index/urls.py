from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name="index"),
    path('', views.homepage, name="homepage"),
    path('about/', views.index, name="about"),
]
