from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.index, name='ShopeHome'),
    path('basic/', views.basic, name='Basic'),
    path('you/', views.you, name='You'),
    path('about/', views.about, name='About'),
    path('contact/', views.contact, name='Contact'),
    path('search/', views.search, name='search'),
    path('Product/<int:myid>/', views.productView, name='ProductView'),
    path('cart/', views.cart, name='Cart'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
  
  
]
