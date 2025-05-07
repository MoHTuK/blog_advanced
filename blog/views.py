from django.views.generic import ListView, DetailView

from blog.models import Blog

# Create your views here.

class PostListView(ListView):
    model = Blog
    context_object_name = 'blogs'
    template_name = 'blog/index.html'


class PostDetailView(DetailView):
    model = Blog
    context_object_name = "blog"
    template_name = 'blog/detail.html'
