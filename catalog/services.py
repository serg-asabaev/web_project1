from django.core.cache import cache

from config.settings import CACHE_ENABLED
from .models import Product, Category


def get_product_from_cache():
    """Получает данные о товаре из кэша, если кэш пуст то возвращает данные из базы"""
    if not CACHE_ENABLED:
        return Product.objects.all()

    key = "products_list"
    products = cache.get(key)
    if products is not None:
        return products

    products = Product.objects.all()
    cache.set(key, products, 60)

    return products

class ProductService:

    @staticmethod
    def get_product_in_category(category:Category):

        key = "category_" + str(category.id)
        products = cache.get(key)
        if products is not None:
            return products

        products = Product.objects.filter(category=category)
        cache.set(key, products, 60)

        return products