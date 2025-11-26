from django.db import models
from django.contrib.auth import get_user_model


# Получаем модель пользователя Django
User = get_user_model()


class Category(models.Model):
    """Модель для тематических категорий постов."""

    title = models.CharField(
        max_length=256,
        verbose_name='Заголовок',
        help_text='Максимальная длина строки — 256 символов'
    )
    description = models.TextField(
        verbose_name='Описание',
        help_text='Подробное описание категории'
    )
    slug = models.SlugField(
        unique=True,
        verbose_name='Слаг',
        help_text='Уникальное значение для URL'
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано',
        help_text='Снимите галочку, чтобы скрыть категорию'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('title',)

    def __str__(self):
        return self.title


class Location(models.Model):
    """Модель для географических меток."""

    name = models.CharField(
        max_length=256,
        verbose_name='Название локации',
        help_text='Максимальная длина строки — 256 символов'
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано',
        help_text='Снимите галочку, чтобы скрыть локацию'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Post(models.Model):
    """Модель для публикаций (постов) в блоге."""

    title = models.CharField(
        max_length=256,
        verbose_name='Заголовок поста',
        help_text='Максимальная длина строки — 256 символов'
    )
    text = models.TextField(
        verbose_name='Основной текст поста',
        help_text='Содержание публикации'
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        help_text='Выберите дату и время публикации'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор',
        help_text='Автор публикации'
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,  # Локация необязательна
        verbose_name='Локация',
        help_text='Местоположение, к которому относится пост (необязательно)'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,  # Позволяет установить NULL при удалении категории
        blank=False,  # Категория обязательна
        verbose_name='Категория',
        help_text='Категория, к которой относится пост'
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано',
        help_text='Снимите галочку, чтобы скрыть публикацию'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата добавления в БД'
    )

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'
        ordering = ('-pub_date',)  # Сортировка по дате

    def __str__(self):
        return self.title
