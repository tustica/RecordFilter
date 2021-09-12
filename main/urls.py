from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('getdata', views.ajaxCall),
    path('datedata', views.datadata),
]