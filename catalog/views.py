from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from catalog.models import Product
from catalog.forms import ProductForm


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

#CRUD
class ProductCreateView(CreateView):
    model = Product
    context_object_name = 'product'
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

class ProductUpdateView(UpdateView):
    model = Product
    context_object_name = 'product'
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

class ProductDeleteView(DeleteView):
    model = Product
    context_object_name = 'product'
    success_url = reverse_lazy('catalog:product_list')