from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView

from catalog.models import Product


class IndexView(TemplateView):
    model = Product
    template_name = "catalog/base.html"

class ContactsView(TemplateView):
    model = Product
    template_name = "catalog/contacts.html"

class ProductListView(ListView):
    model = Product
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'

