from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Category
from django.db.models import Q


def index(request):
    now = timezone.now()
    posts = Post.objects.filter(
        pub_date__lte=now,
        is_published=True,
        category__is_published=True
    ).filter(
        Q(location__isnull=True) | Q(location__is_published=True)
    ).order_by('-pub_date')[:5]
    return render(request, 'blog/index.html', {'posts': posts})


# Переименовываем функцию 'category' в 'category_posts'
def category_posts(request, slug):
    category = get_object_or_404(Category, slug=slug, is_published=True)
    now = timezone.now()
    posts = Post.objects.filter(
        category=category,
        is_published=True,
        pub_date__lte=now
    ).filter(
        Q(location__isnull=True) | Q(location__is_published=True)
    ).order_by('-pub_date')
    return render(request, 'blog/category.html',
                  {'category': category, 'posts': posts})


# Обновляем функцию 'post_detail' для более строгой проверки location
def post_detail(request, pk):
    now = timezone.now()
    post = get_object_or_404(
        Post.objects.filter(
            is_published=True,
            pub_date__lte=now,
            category__is_published=True,
        ).filter(
            Q(location__isnull=True) | Q(location__is_published=True)
        ),
        pk=pk
    )
    return render(request, 'blog/detail.html', {'post': post})
