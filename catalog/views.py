from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseForbidden
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.core.cache import cache
from unicodedata import category

from catalog.models import Product, Category
from catalog.forms import ProductForm, ProductModeratorForm
from .services import get_product_from_cache, ProductService


class IndexView(TemplateView):
    model = Product
    template_name = "catalog/base.html"

class ContactsView(TemplateView):
    model = Product
    template_name = "catalog/contacts.html"

class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'
    login_url = reverse_lazy('users:login')

    def get_queryset(self):
        if not self.request.user.has_perm('catalog.view_product'):
            return Product.objects.none()
        return get_product_from_cache()

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

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    context_object_name = 'product'
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')
    login_url = reverse_lazy('users:login')

    def get_form_class(self):
        user = self.request.user

        if user == self.object.owner:
            return ProductForm

        if user.has_perm('catalog.can_unpublish_product'):
            return ProductModeratorForm

        raise PermissionDenied

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    context_object_name = 'product'
    success_url = reverse_lazy('catalog:product_list')
    login_url = reverse_lazy('users:login')

class ProductPublishView(LoginRequiredMixin, View):

    def post(self, request, pk):
        product = get_object_or_404(Product, id=pk)

        if not request.user.has_perm('catalog.can_unpublish_product'):
            return HttpResponseForbidden("У вас нет права отменять публикацию товара!")

        product.is_published = False
        product.save()

        return redirect('catalog:product_update', pk=product.id)

class CategoryDetailView(DetailView):
    model = Category
    template_name = "catalog/category_detail.html"
    context_object_name = "category"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = Category.objects.get(id=self.kwargs['pk'])
        context['products'] = ProductService.get_product_in_category(category)
        context['category_name'] = category.name
        return context