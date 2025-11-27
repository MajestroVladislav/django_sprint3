from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.utils import timezone
from django.conf import settings


def index(request):
    posts = Post.objects.select_related(
        'category', 'location', 'author'
    ).filter(
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True
    ).order_by('-pub_date')[:settings.NUMBER_OF_POSTS_ON_MAIN_PAGE]

    context = {
        'posts': posts,
    }
    return render(request, 'blog/index.html', context)


def post_detail(request, id):
    post = get_object_or_404(
        Post.objects.select_related('category',
                                    'location', 'author').filter(
            is_published=True,
            pub_date__lte=timezone.now(),
            category__is_published=True
        ),
        pk=id
    )

    context = {
        'post': post,
    }
    return render(request, 'blog/detail.html', context)


def category_posts(request, slug):
    category = get_object_or_404(
        Category,
        is_published=True,
        slug=slug
    )

    posts = Post.objects.select_related(
        'category', 'location', 'author'
    ).filter(
        category=category,
        is_published=True,
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')

    context = {
        'category': category,
        'posts': posts,
    }
    return render(request, 'blog/category.html', context)
