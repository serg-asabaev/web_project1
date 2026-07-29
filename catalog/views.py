from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

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

class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    context_object_name = 'product'
    login_url = reverse_lazy('users:login')

#CRUD
class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    context_object_name = 'product'
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')
    login_url = reverse_lazy('users:login')

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    context_object_name = 'product'
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')
    login_url = reverse_lazy('users:login')

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    context_object_name = 'product'
    success_url = reverse_lazy('catalog:product_list')
    login_url = reverse_lazy('users:login')