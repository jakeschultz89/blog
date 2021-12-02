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

class BlogListView(ListView):
    model = Post
    template_name = "blog_list.html"

class BlogDetailView(DetailView):
    model = Post
    template_name = "blog_detail.html"

class BlogCreateView(CreateView):
    model = Post
    template_name = "blog_new.html"
    fields = ["title", "body", "author"]

class BlogUpdateView(UpdateView):
    model = Post
    template_name = "blog_edit.html"
    fields = ["title", "body"]

class BlogDeleteView(DeleteView):
    model = Post
    template_name = "blog_delete.html"
    success_url = reverse_lazy("blog_list")