from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('/ringing-equipment', views.ringing_equipment, name='ringing_equipment'),
    path('/merchandise', views.merchandise, name='merchandise'),
]
