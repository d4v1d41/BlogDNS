from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Post
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    posts_list = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')[::-1]
    page = request.GET.get('page', 1)
    paginator = Paginator(posts_list, 6)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    template = loader.get_template('blog/index.html')
    context= {'posts': posts}
    return HttpResponse(template.render(context, request))
    # POSTS


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    template = loader.get_template('blog/detail.html')
    context = {'post': post}
    return HttpResponse(template.render(context, request))