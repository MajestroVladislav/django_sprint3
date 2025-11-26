from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.db.models import Q, F
from .models import Post, Category


def index(request):
    now = timezone.now()
    posts = Post.objects.filter(
        pub_date__lte=now,
        is_published=True,
        category__is_published=True
    ).annotate(
        location_is_published=F('location__is_published')
    ).filter(
        Q(location__isnull=True) | Q(location_is_published=True)
    ).order_by('-pub_date')[:5]
    context = {
        'title': 'Главная страница блога',
        'posts': posts
    }
    print("DEBUG context keys:", list(context.keys()))
    return render(request, 'blog/index.html', context)


def category_posts(request, slug):
    category = get_object_or_404(Category, slug=slug,
                                 is_published=True)
    now = timezone.now()
    posts = Post.objects.filter(
        category=category,
        is_published=True,
        pub_date__lte=now
    ).annotate(
        location_is_published=F('location__is_published')
    ).filter(
        Q(location__isnull=True) | Q(location_is_published=True)
    ).order_by('-pub_date')
    context = {
        'category': category,
        'posts': posts,
        'slug': slug,
        'title': category.title
    }
    print("DEBUG context keys:", list(context.keys()))
    return render(request, 'blog/category.html', context)


def post_detail(request, id):
    now = timezone.now()
    post = get_object_or_404(
        Post.objects.filter(
            is_published=True,
            pub_date__lte=now,
            category__is_published=True,
        ).annotate(
            location_is_published=F('location__is_published')
        ).filter(
            Q(location__isnull=True) | Q(location_is_published=True)
        ),
        pk=id
    )
    context = {
        'post': post,
        'title': post.title,
        'text': post.text,
    }
    print("DEBUG context keys:", list(context.keys()))
    return render(request, 'blog/detail.html', context)
