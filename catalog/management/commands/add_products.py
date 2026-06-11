from django.core.management.base import BaseCommand
from catalog.models import Category, Product

class Command(BaseCommand):

    help = 'add category to the database'

    def handle(self, *args, **options):

        Category.objects.all().delete()
        Products.objects.all().delete()

        category, _ = Category.objects.get_or_create(name='Смартфон', description='Все смартфоны')

        products = [
            {
                'name': 'Iphone 17 Pro',
                'description': 'Смартфон APPLE iPhone 17 Pro 256GB Lavender - eSIM A3258 /A3519 - MG7L4/MG6A4>',
                'category': category,
                'price': 100000
             },
            {
                'name': 'Poco X4 GT',
                'description': 'Смартфон Poco X4 GT 128GB Grey',
                'category': category,
                'price': 30000
            }
        ]

        for products_data in products:

            product, created = Product.objects.get_or_create(**products_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added product: {product.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Book already exists: {product.name}'))