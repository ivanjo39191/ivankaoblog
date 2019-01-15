from django.shortcuts import render,get_object_or_404
from .models import Blog, BlogType
#文章詳細頁面需要使用到通用模型
from comment.forms import CommentForm
from django.contrib.contenttypes.models import ContentType
from comment.models import Comment
from django.db.models import Count
# Create your views here.

def common_blog(request,blog_all_list):

    blog_type_count = BlogType.objects.annotate(blog_count=Count('blog')).order_by('-id') 
    context = {}
    context['blogs'] = blog_all_list
    context['blog_types'] = blog_type_count

    return context

def blog_list(request):

    blog_all_list = Blog.objects.all()
    context = common_blog(request,blog_all_list)
    
    return render(request,"blog_list.html",context)


def blog_type(request, type_pk):

    blog_all_list = Blog.objects.filter(blogtype=type_pk)
    context = common_blog(request,blog_all_list)

    return render(request, "blog_type.html", context )

def blog_detail(request, blog_pk):

    blog_detail = Blog.objects.filter(pk=blog_pk)
    context = {}
    blog = get_object_or_404(Blog, pk=blog_pk)  #獲取blog_pk
    context['blogs'] = blog_detail
    #取得該評論對應的文章類型與編號
    blog_content_type = ContentType.objects.get_for_model(blog)
    comments = Comment.objects.filter(content_type=blog_content_type, object_id=blog.pk)
        #使用initial在運行時聲明表單字段的初始值，將文章類型與編號賦值
    data={}
    data['content_type']= blog_content_type.model
    data['object_id'] = blog_pk
    context['comment_form'] = CommentForm(initial=data)
    context['comments'] = comments
 
    response = render(request, 'blog_detail.html', context) #將字典返回到'blog_detail.html'
    return response



