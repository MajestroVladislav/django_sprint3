from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Category, Location, Post


admin.site.site_title = _("Блог")
admin.site.site_header = _("Блог")
admin.site.index_title = _("Управление")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "is_published")
    list_filter = ("is_published",)
    search_fields = ("title", "slug")
    fieldsets = (
    (None, {
    "fields": ("title", "description", "slug", "is_published"),
    }),
    )


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "is_published")
    list_filter = ("is_published",)
    search_fields = ("name",)
    fieldsets = (
    (None, {
    "fields": ("name", "is_published"),
    }),
    )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "pub_date", "is_published")
    list_filter = ("is_published", "pub_date", "category")
    search_fields = ("title", "text", "author__username")
    fieldsets = (
    (None, {
    "fields": ("title", "text", "pub_date", "author",
               "category", "location", "is_published"),
    }),
    )
