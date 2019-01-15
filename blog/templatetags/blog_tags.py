from django import template
from ..models import Blog,BlogType
from django.contrib.contenttypes.models import ContentType

register = template.Library()


@register.simple_tag
def type_name_blog(type_name):
    type_blog = Blog.objects.filter(blogtype=type_name)[:5]
    return type_blog