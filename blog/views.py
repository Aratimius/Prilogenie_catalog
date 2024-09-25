from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from pytils.translit import slugify

from blog.models import Blog
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView


class BlogListView(ListView):
    model = Blog

    def get_queryset(self):
        """Фильтрация по опубликованным статьсям"""
        queryset = super().get_queryset()
        queryset = queryset.filter(publication_sign=True)
        return queryset


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'content', 'preview', 'publication_sign')
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        """Автоматическое создание slug"""
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'content', 'preview', 'publication_sign')

    def get_success_url(self):
        """Перенаправление после редактирования на просмотр блога"""
        return reverse("blog:detail", args=[self.kwargs.get("pk")])


class BlogDetailView(DetailView):
    model = Blog

    def get_context_data(self, **kwargs):
        """Передать объекту заголовок статьи"""
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = Blog.objects.get(pk=self.kwargs['pk'])
        return context_data

    def get_object(self, queryset=None):
        """Метод для увеличения счетчика просмотров"""
        self.object = super().get_object(queryset)
        self.object.views += 1
        self.object.save()
        return self.object


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:list')
