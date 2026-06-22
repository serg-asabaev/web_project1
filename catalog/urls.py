from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.index, name='index'),
    path('contacts/', views.contacts, name='contacts'),
    path('products/detail/<int:pk>/', views.product_details, name='products_detail'),
    path('products/list/', views.product_list, name='products_list')
]