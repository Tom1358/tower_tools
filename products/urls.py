from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('ringing_equipment/', views.ringing_equipment, name='products/ringing_equipment'),
    path('merchandise/', views.merchandise, name='products/merchandise'),
    path('learning_tools/', views.learning_tools, name='products/learning_tools'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
]
