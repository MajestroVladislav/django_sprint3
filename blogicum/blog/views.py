from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Category


def index(request):  # Главная страница
    now = timezone.now()
    posts = Post.objects.filter(pub_date__lte=now,
                                is_published=True,
                                category__is_published=True).order_by('-pub_date')[:5]
    return render(request, 'blog/index.html', {'posts': posts})


def category(request, slug):  # Страница категории
    category = get_object_or_404(Category, slug=slug, is_published=True)
    now = timezone.now()
    posts = Post.objects.filter(category=category, is_published=True,
                                pub_date__lte=now).order_by('-pub_date')
    return render(request, 'blog/category.html',
                  {'category': category, 'posts': posts})


def post_detail(request, pk):  # Страница поста:
    now = timezone.now()
    post = get_object_or_404(Post, pk=pk, is_published=True,
                             pub_date__lte=now, category__is_published=True)
    return render(request, 'blog/detail.html', {'post': post})
