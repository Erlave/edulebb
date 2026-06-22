from django.db import models
from django.urls import reverse

# Create your models here.
from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Instructor(models.Model):
    full_name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="instructors/")
    position = models.CharField(max_length=100, blank=True)
    bio = models.TextField()

    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    instagram = models.URLField(blank=True)

    class Meta:
        verbose_name = "مدرس"
        verbose_name_plural = "مدرسان"

    def __str__(self):
        return self.full_name


class Course(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True, blank=True)

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="courses"
    )

    instructor = models.ForeignKey(
        Instructor,
        on_delete=models.SET_NULL,
        null=True,
        related_name="courses"
    )

    image = models.ImageField(upload_to="courses/")
    short_description = models.CharField(max_length=300)
    description = models.TextField()
    Study_program = models.TextField(blank=True,null=True)

    price = models.PositiveIntegerField(default=0)

    duration = models.CharField(max_length=100)
    total_lectures = models.PositiveIntegerField(default=0)
    students_count = models.PositiveIntegerField(default=0)
    available_seats = models.PositiveIntegerField(default=0)

    has_certificate = models.BooleanField(default=True)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "دوره"
        verbose_name_plural = "دوره ها"


    def get_absolute_url(self):
        return reverse("course-details", args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Review(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="reviews"
    )

    name = models.CharField(max_length=120)
    email = models.EmailField()

    rate = models.PositiveSmallIntegerField(default=5)

    comment = models.TextField()
    is_active = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "نظر"
        verbose_name_plural = "نظرات"

    def __str__(self):
        return f"{self.name} - {self.course.title}"