from django.db import models
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class Instructor(models.Model):
    full_name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="instructors/")
    position = models.CharField(max_length=100, blank=True)
    bio = models.TextField()
    slug = models.SlugField(unique=True, blank=True)


    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    instagram = models.URLField(blank=True)


    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    skype = models.CharField(max_length=100, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.full_name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "مدرس"
        verbose_name_plural = "مدرسان"

    def __str__(self):
        return self.full_name
