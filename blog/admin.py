from django.contrib import admin
from .models import Blog,BlogAuthor, BlogCategory,BlogComment


# Register your models here.







@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):

    list_display = (
        "title",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }

    search_fields = (
        "title",
    )


@admin.register(BlogAuthor)
class BlogAuthorAdmin(admin.ModelAdmin):

    list_display = (
        "full_name",
    )

    search_fields = (
        "full_name",
    )


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "category",
        "author",
        "created_at",
        "views",
        "is_active",
    )

    list_filter = (
        "category",
        "author",
        "is_active",
    )

    list_editable = (
        "is_active",
    )

    search_fields = (
        "title",
        "short_description",
        "content",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }

    autocomplete_fields = (
        "category",
        "author",
    )


@admin.register(BlogComment)
class BlogCommentAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "blog",
        "created_at",
        "is_active",
    )

    list_filter = (
        "is_active",
    )

    list_editable = (
        "is_active",
    )

    search_fields = (
        "name",
        "email",
        "message",
    )

    autocomplete_fields = (
        "blog",
    )