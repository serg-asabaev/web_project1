from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from catalog.apps import CatalogConfig
from config.settings import MEDIA_ROOT

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("catalog.urls", namespace='catalog')),
    path("blog/", include("blog.urls", namespace='blog')),
]

if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=MEDIA_ROOT)
