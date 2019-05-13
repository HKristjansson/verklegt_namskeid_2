from django.urls import path
from .views import PostListView

from . import views

urlpatterns = [
    path('', PostListView.as_view(), name="index"),
    # path('', views.index, name="index"),
    path('about/', views.about, name="about"),
]
