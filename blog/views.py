from django.shortcuts import render

from django.urls import reverse_lazy, reverse
from django.utils.text import slugify
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from blog.models import Blog


class BlogListView(ListView):
    model = Blog
    fields = ("title", "content", "preview", "created_at")
    success_url = reverse_lazy("blog:blog_list")


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.number_of_views += 1
        self.object.save()
        return self.object


class BlogCreateView(CreateView):
    model = Blog
    fields = ("title", "content", "preview", "created_at")
    success_url = reverse_lazy("blog:blog_list")

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ("title", "content", "preview", "created_at")

    def get_success_url(self):
        return reverse("blog:blog_detail", kwargs={"pk": self.object.pk})


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy("blog:blog_list")
