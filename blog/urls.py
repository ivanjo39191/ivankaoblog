from django.urls import path
from . import views, pixnetcrawler

urlpatterns = [

    path('',views.blog_list,name="blog_list"),
    path('pixnetcrawler', pixnetcrawler.pixnetcrawler, name='pixnetcrawler'),
    path('blog_type/<int:type_pk>',views.blog_type,name="blog_type"),
    path('blog_detail/<int:blog_pk>', views.blog_detail, name="blog_detail"),
]