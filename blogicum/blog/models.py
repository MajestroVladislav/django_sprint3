from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

# Получаем модель пользователя Django
User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # Добавляем новые поля
    field1 = models.CharField(max_length=200, default='default_value')
    field2 = models.CharField(max_length=200, default='default_value')
    field3 = models.CharField(max_length=200, default='default_value')
    field4 = models.CharField(max_length=200, default='default_value')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Location(models.Model):
    name = models.CharField('Название места',
                            max_length=256)
    is_published = models.BooleanField('Опубликовано',
                                       default=True)
    created_at = models.DateTimeField('Добавлено',
                                      auto_now_add=True)

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField('Заголовок', max_length=256)
    text = models.TextField('Текст')
    pub_date = models.DateTimeField(
        'Дата и время публикации',
        default=timezone.now,
        help_text='Если установить дату и время в будущем'
                  ' — можно делать отложенные публикации.'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор публикации'
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Местоположение'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        verbose_name='Категория'
    )
    is_published = models.BooleanField('Опубликовано',
                                       default=True)
    created_at = models.DateTimeField('Добавлено',
                                      auto_now_add=True)

    field1 = models.CharField(max_length=200, default='default_value')
    field2 = models.CharField(max_length=200, default='default_value')
    field3 = models.CharField(max_length=200, default='default_value')

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'
        ordering = ('-pub_date',)

    def __str__(self):
        return self.title
