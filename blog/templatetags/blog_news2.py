from django import template
from ..models import Blog,BlogType
from django.contrib.contenttypes.models import ContentType

register = template.Library()

@register.simple_tag
def blog_name_newest2():
    blog_newest2 = Blog.objects.all()[5:10]
    return blog_newest2
