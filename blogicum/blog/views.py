from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.db.models import Q
from django.utils import timezone
from django.conf import settings


def index(request):
    # Используем select_related для оптимизации и гарантии загрузки связанных объектов
    posts = Post.objects.select_related(
        'category', 'location', 'author'
    ).filter(
        is_published=True,
        pub_date__lte=timezone.now(),
        Q(category__isnull=True) | Q(category__is_published=True),
        Q(location__isnull=True) | Q(location__is_published=True),
    ).order_by('-pub_date')[:settings.NUMBER_OF_POSTS_ON_MAIN_PAGE]

    context = {
        'title': 'Главная страница',
        'posts': posts,
    }
    return render(request, 'blog/index.html', context)


def post_detail(request, id):
    # Используем select_related для оптимизации и гарантии загрузки связанных объектов
    post = get_object_or_404(
        Post.objects.select_related('category', 'location', 'author'),
        pk=id,
        is_published=True,
        pub_date__lte=timezone.now(),
        Q(category__isnull=True) | Q(category__is_published=True),
        Q(location__isnull=True) | Q(location__is_published=True),
    )
    context = {
        'title': post.title,
        'post': post,
    }
    return render(request, 'blog/detail.html', context)


def category_posts(request, slug):
    # Категория должна быть опубликована
    category = get_object_or_404(
        Category.objects.filter(is_published=True),
        slug=slug
    )
    posts = Post.objects.select_related(
        'category', 'location', 'author'
    ).filter(
        category=category,
        is_published=True,
        pub_date__lte=timezone.now(),
        Q(location__isnull=True) | Q(location__is_published=True),
    ).order_by('-pub_date')

    context = {
        'title': f'Записи категории "{category.title}"',
        'category': category,
        'posts': posts,
    }
    return render(request, 'blog/category.html', context)
