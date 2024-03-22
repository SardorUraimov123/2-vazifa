from django.shortcuts import render, get_object_or_404, redirect
from .models import News, Region, Category, Post, PostImg, PostVideo, Comment

def index(request):
    news = News.objects.all()
    regions = Region.objects.all()
    categories = Category.objects.all()
    
    context = {
        'news': news,
        'regions': regions,
        'categories': categories,
    }
    return render(request, 'index.html', context)

def post_detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    post_images = PostImg.objects.filter(post=post)
    post_videos = PostVideo.objects.filter(post=post)
    comments = Comment.objects.filter(post=post)
    
    context = {
        'post': post,
        'post_images': post_images,
        'post_videos': post_videos,
        'comments': comments,
    }
    return render(request, 'front/post_detail.html', context)

def news_detail_single(request, news_id): 
    news_item = News.objects.get(pk=news_id)
    
    context = {
        'news_item': news_item,
    }
    return render(request, 'front/news_detail.html', context)

def about(request):
    return render(request, 'about.html')

def action(request):
    return render(request, 'action.html')

def contact(request):
    categories = Category.objects.all()
    regions = Region.objects.all()
    context = {
        'categories': categories,
        'regions': regions,
    }
    return render(request, 'contact.html', context)

def doctores(request):
    return render(request, 'doctores.html')

def news_list(request):
    news = News.objects.all()
    return render(request, 'news_list.html', {'news': news})

def news_detail(request, pk):
    news = get_object_or_404(News, pk=pk)
    return render(request, 'news_detail.html', {'news': news})
