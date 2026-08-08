from django.urls import path
from django.views.decorators.cache import cache_page

from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('contacts/', views.ContactsView.as_view(), name='contacts'),
    path('products/<int:pk>/detail/',cache_page(60)(views.ProductDetailView.as_view()), name='product_detail'),
    path('products/list/', views.ProductListView.as_view(), name='product_list'),
    path('products/create/', views.ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/update/', views.ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product_delete'),
    path('products/<int:pk>/unpublish/', views.ProductPublishView.as_view(), name='product_unpublish'),
    path('products/<int:pk>/category_detail/', views.CategoryDetailView.as_view(), name='category_detail'),
]