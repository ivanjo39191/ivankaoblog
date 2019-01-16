from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField #導入富文本套件

# Create your models here.
class BlogType(models.Model):
    type_name = models.CharField(max_length=200,null=True)
    last_updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.type_name


class Blog(models.Model):

    blogtitle = models.CharField(max_length=200,null=True)
    blogcontent = RichTextUploadingField() #改為RichTextField
    blogtype = models.ForeignKey(BlogType, on_delete=models.CASCADE)
    blogauthor = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    blog_time = models.CharField(max_length=200,null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    last_updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.blogtitle

    class Meta:
        ordering = ['-created_time']