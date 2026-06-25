from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.models import BlogRecord

class BlogIndexView(TemplateView):
    model = BlogRecord
    template_name = ""

class BlogListView(ListView):
    model = BlogRecord
    context_object_name = 'blog'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(published=True)

class BlogDetailView(DetailView):
    model = BlogRecord
    context_object_name = 'blog_record'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object

class BlogCreateView(CreateView):
    model = BlogRecord
    context_object_name = 'blog_record'
    fields = ('title', 'content', 'preview', 'published')
    success_url = reverse_lazy('blog:blog_list')

class BlogUpdateView(UpdateView):
    model = BlogRecord
    context_object_name = 'blog_record'
    fields = ('title', 'content', 'preview', 'published')
    success_url = reverse_lazy('blog:blog_list')

    def get_success_url(self):
        return reverse('blog:blog_detail', args=[self.kwargs.get('pk')])

class BlogDeleteView(DeleteView):
    model = BlogRecord
    context_object_name = 'blog_record'
    success_url = reverse_lazy('blog:blog_list')