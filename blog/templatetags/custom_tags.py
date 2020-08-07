from django import template
from blog.models import Post, Category, Tag

register = template.Library()


@register.simple_tag(name="categories")
def all_categories():
    return Category.objects.all()


@register.simple_tag(name="tags")
def all_tags():
    return Tag.objects.all()