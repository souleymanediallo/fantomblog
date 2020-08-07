from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Post, Category, Tag


# Create your views here.
def home(request):
    return render(request, "blog/index.html")


class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"


class PostDetailView(DetailView):
    model = Post
    slug_field = "slug"
    template_name = "blog/post_detail.html"
    context_object_name = "post"


class PostCategoryView(ListView):
    model = Post
    template_name = "post/post_by_category.html"
    context_object_name = "posts"

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['category'])
        return Post.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.category = get_object_or_404(Category, slug=self.kwargs['category'])
        context['category'] = self.category
        return context


class TagListView(ListView):
    model = Post
    template_name = "post_by_tag.html"
    context_object_name = "posts"

    def get_queryset(self):
        self.title = get_object_or_404(Tag, slug=self.kwargs['tag'])
        return Post.objects.filter(tag=self.title)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.title = get_object_or_404(Tag, slug=self.kwargs['tag'])
        context['tags'] = self.title
        return context
