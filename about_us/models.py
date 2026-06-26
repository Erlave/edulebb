from django.db import models

# Create your models here.



class AboutPage(models.Model):
    title = models.CharField(max_length=255)
    description_1 = models.TextField()
    description_2 = models.TextField()

    image = models.ImageField(upload_to="about/")

    video_url = models.URLField(blank=True)

    button_text = models.CharField(
        max_length=100,
        default="مشاهده دوره ها"
    )

    button_url = models.CharField(
        max_length=255,
        blank=True
    )


    def save(self, *args, **kwargs):
        if not self.pk and AboutPage.objects.exists():
            raise ValueError(
                "Only one AboutPage instance is allowed."
            )

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "درباره ما"
        verbose_name_plural = "درباره ما"

    def __str__(self):
        return self.title


class AboutFeature(models.Model):
    about = models.ForeignKey(
        AboutPage,
        on_delete=models.CASCADE,
        related_name="features"
    )

    title = models.CharField(max_length=150)
    short_description = models.TextField()

    order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ["order"]
        verbose_name = "ویژگی"
        verbose_name_plural = "ویژگی ها"

    def __str__(self):
        return self.title


class AboutBenefit(models.Model):
    about = models.ForeignKey(
        AboutPage,
        on_delete=models.CASCADE,
        related_name="benefits"
    )

    title = models.CharField(max_length=255)

    order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ["order"]
        verbose_name = "مزیت"
        verbose_name_plural = "مزیت ها"

    def __str__(self):
        return self.title


class AboutCounter(models.Model):
    title = models.CharField(max_length=150)

    value = models.PositiveIntegerField()

    icon_class = models.CharField(
        max_length=50,
        help_text="مثال : ti-folder"
    )

    order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ["order"]
        verbose_name = "آمار"
        verbose_name_plural = "آمار ها"

    def __str__(self):
        return self.title


class AboutBanner(models.Model):
    title = models.CharField(max_length=200)

    subtitle = models.CharField(max_length=200)

    description = models.TextField()

    image = models.ImageField(
        upload_to="about/banners/"
    )

    button_text = models.CharField(max_length=100)

    button_url = models.CharField(max_length=255)

    order = models.PositiveIntegerField(default=1)

    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]
        verbose_name = "بنر"
        verbose_name_plural = "بنر ها"

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    full_name = models.CharField(max_length=200)

    company = models.CharField(
        max_length=200,
        blank=True
    )

    image = models.ImageField(
        upload_to="about/testimonials/"
    )

    text = models.TextField()

    rate = models.PositiveSmallIntegerField(default=5)

    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "نظر دانشجو"
        verbose_name_plural = "نظرات دانشجویان"

    def __str__(self):
        return self.full_name
    



class FAQPage(models.Model):
    image = models.ImageField(upload_to="faq/")

    class Meta:
        verbose_name = "صفحه سوالات متداول"
        verbose_name_plural = "صفحه سوالات متداول"

    def __str__(self):
        return "FAQ Page"


class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    order = models.PositiveIntegerField(default=1)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]
        verbose_name = "سوال"
        verbose_name_plural = "سوالات"

    def __str__(self):
        return self.question