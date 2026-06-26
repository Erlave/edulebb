from django.db import models


class SiteSetting(models.Model):
    # Header
    site_name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to="site/logo/")
    favicon = models.ImageField(upload_to="site/favicon/", blank=True)

    # Hero Section
    hero_title = models.CharField(max_length=250)
    hero_description = models.TextField()
    hero_image = models.ImageField(upload_to="site/hero/")

    # Footer
    footer_description = models.TextField()

    # Contact
    address = models.TextField()
    phone = models.CharField(max_length=30)
    email = models.EmailField()

    # Social Media
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)

    # SEO
    meta_description = models.TextField(blank=True)

    # Copyright
    copyright = models.CharField(max_length=200)

    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "تنظیمات سایت"
        verbose_name_plural = "تنظیمات سایت"

    def __str__(self):
        return self.site_name


class FooterBox(models.Model):
    title = models.CharField(max_length=100)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = "باکس فوتر"
        verbose_name_plural = "باکس‌های فوتر"

    def __str__(self):
        return self.title


class FooterLink(models.Model):
    footer_box = models.ForeignKey(
        FooterBox,
        on_delete=models.CASCADE,
        related_name="links"
    )

    title = models.CharField(max_length=100)

    url = models.CharField(max_length=255)

    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = "لینک فوتر"
        verbose_name_plural = "لینک‌های فوتر"

    def __str__(self):
        return self.title