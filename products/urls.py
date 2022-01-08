from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('ringing_equipment', views.ringing_equipment, name='products/ringing_equipment'),
    path('merchandise', views.merchandise, name='products/merchandise'),
    path('learning_tools', views.learning_tools, name='products/learning_tools'),
    path('<product_id>', views.product_detail, name='product_detail'),
]
