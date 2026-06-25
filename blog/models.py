from django.db import models

class BlogRecord(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Текст записи')
    preview = models.ImageField(upload_to='blog/images', blank=True, null=True, verbose_name='Превью')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    published = models.BooleanField(default=False, verbose_name='Признак публикации')

    views_count = models.PositiveIntegerField(default=0, verbose_name="Количество просмотров")

    def __str__(self):
        return f'{self.title}: {self.content}'

    class Meta:
        verbose_name = 'Запись блога'
        verbose_name_plural = 'Записи блога'
        ordering = ['title',]