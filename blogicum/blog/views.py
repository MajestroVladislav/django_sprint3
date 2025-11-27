from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.conf import settings
from .models import Post, Category


def index(request):
    post_list = Post.objects.select_related(
        'category', 'location', 'author'
    ).filter(
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True
    ).order_by('-pub_date')[:settings.NUMBER_OF_POSTS_ON_MAIN_PAGE]

    return render(request, 'blog/index.html', {'posts': post_list})


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
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, slug):
    category = get_object_or_404(
        Category.objects.filter(is_published=True),
        slug=slug
    )

    post_list = Post.objects.select_related(
        'category', 'location', 'author'
    ).filter(
        category=category,
        is_published=True,
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')

    return render(request, 'blog/category.html', {
        'category': category,
        'posts': post_list
    })
