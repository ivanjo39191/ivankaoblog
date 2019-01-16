from django import template
from ..models import Blog,BlogType
from django.contrib.contenttypes.models import ContentType

register = template.Library()

@register.simple_tag
def blog_name_newest():
    blog_newest = Blog.objects.all()[:5]
    return blog_newest
