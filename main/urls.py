from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add', views.addRecord),
    path('getdata', views.ajaxCall),
    path('datedata', views.datadata),
]