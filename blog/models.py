from django.db import models
from django.urls import reverse


# Create your models here.




class BlogCategory(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"
        ordering = ["title"]

    def __str__(self):
        return self.title


class BlogAuthor(models.Model):
    full_name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="blog/authors/")
    bio = models.TextField()

    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)

    class Meta:
        verbose_name = "نویسنده"
        verbose_name_plural = "نویسندگان"

    def __str__(self):
        return self.full_name


class Blog(models.Model):
    category = models.ForeignKey(
        BlogCategory,
        on_delete=models.CASCADE,
        related_name="blogs"
    )

    author = models.ForeignKey(
        BlogAuthor,
        on_delete=models.CASCADE,
        related_name="blogs"
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)

    image = models.ImageField(upload_to="blog/posts/")

    short_description = models.TextField(
        help_text="برای کارت مقاله"
    )

    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    views = models.PositiveIntegerField(default=0)

    is_active = models.BooleanField(default=True)

    @property
    def comments_count(self):
        return self.comments.filter(
            is_active=True
        ).count()

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "blog_detail",
            args=[self.slug]
        )


class BlogComment(models.Model):
    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        related_name="comments"
    )

    name = models.CharField(max_length=120)

    email = models.EmailField()

    subject = models.CharField(max_length=200)

    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "نظر"
        verbose_name_plural = "نظرات"

    def __str__(self):
        return f"{self.name} - {self.blog.title}"