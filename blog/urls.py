from django.contrib import admin
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.BlogIndexView.as_view(), name='index'),
    path('list/', views.BlogListView.as_view(), name='blog_list'),
    path('blog/<int:pk>/detail/', views.BlogDetailView.as_view(), name='blog_detail'),
    path('blog/create/', views.BlogCreateView.as_view(), name='blog_create'),
    path('blog/<int:pk>/update/', views.BlogUpdateView.as_view(), name='blog_update'),
    path('blog/<int:pk>/delete/', views.BlogDeleteView.as_view(), name='blog_delete'),
]