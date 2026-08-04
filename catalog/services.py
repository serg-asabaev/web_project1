from django.core.cache import cache

from config.settings import CACHE_ENABLED
from users.admin import Product


def get_product_from_cache():
    """Получает данные о товаре из кэша, если кэш пуст то возвращает данные из базы"""
    if not CACHE_ENABLED:
        return Product.objects.all()

    key = "products_list"
    products = cache.get(key)
    if products is not None:
        return products

    products = Product.objects.all()
    cache.set(key, products)

    return products