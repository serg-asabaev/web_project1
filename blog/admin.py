from django.contrib import admin
from .models import BlogRecord

@admin.register(BlogRecord)
class BlogRecord(admin.ModelAdmin):
    list_display = ('title', 'content', )
    search_fields = ('title', 'content', )