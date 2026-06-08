from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'{self.name}: {self.decription}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name',]


class Product(models.Model):

    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='product/images', blank=True, null=True, verbose_name='Изображение')

    # категория,
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='Категория')
    # цена за покупку,
    price = models.FloatField(verbose_name='Цена за покупку')
    # дата создания,
    created_at = models.DateTimeField(verbose_name='Дата создания')
    # дата последнего изменения.
    updated_at = models.DateTimeField(verbose_name='Дата последнего изменения')

    def __str__(self):
        return f'{self.name}: {self.decription}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['name',]