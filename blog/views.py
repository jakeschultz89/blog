from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.views.generic import (
    TemplateView, 
    DetailView, 
    ListView,
)
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

from .models import Post

class HomePageView(TemplateView):
    template_name = 'index.html'

class BlogListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "blog_list.html"

class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = "blog_detail.html"

class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "blog_new.html"
    fields = ["title", "body"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = "blog_edit.html"
    fields = ["title", "body"]

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog_delete.html"
    success_url = reverse_lazy("blog_list")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user