from django.contrib import admin

from .models import AboutPage, AboutFeature ,AboutBenefit, AboutCounter , AboutBanner, Testimonial ,FAQPage, FAQ


class AboutFeatureInline(admin.TabularInline):
    model = AboutFeature
    extra = 1


class AboutBenefitInline(admin.TabularInline):
    model = AboutBenefit
    extra = 1


@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return not AboutPage.objects.exists()
    
    list_display = (
        "title",
    )

    inlines = [
        AboutFeatureInline,
        AboutBenefitInline,
    ]


@admin.register(AboutCounter)
class AboutCounterAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "value",
        "order",
    )

    list_editable = (
        "value",
        "order",
    )

    ordering = (
        "order",
    )

    search_fields = (
        "title",
    )


@admin.register(AboutBanner)
class AboutBannerAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "subtitle",
        "is_active",
        "order",
    )

    list_filter = (
        "is_active",
    )

    list_editable = (
        "is_active",
        "order",
    )

    search_fields = (
        "title",
        "subtitle",
    )

    ordering = (
        "order",
    )


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "company",
        "rate",
        "is_active",
    )

    list_filter = (
        "rate",
        "is_active",
    )

    list_editable = (
        "rate",
        "is_active",
    )

    search_fields = (
        "full_name",
        "company",
    )


@admin.register(AboutFeature)
class AboutFeatureAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "order",
    )

    list_editable = (
        "order",
    )

    ordering = (
        "order",
    )

    search_fields = (
        "title",
    )


@admin.register(AboutBenefit)
class AboutBenefitAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "order",
    )

    list_editable = (
        "order",
    )

    ordering = (
        "order",
    )

    search_fields = (
        "title",
    )




@admin.register(FAQPage)
class FAQPageAdmin(admin.ModelAdmin):

    list_display = ("id",)

    def has_add_permission(self, request):
        return not FAQPage.objects.exists()


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):

    list_display = (
        "question",
        "order",
        "is_active",
    )

    list_editable = (
        "order",
        "is_active",
    )

    search_fields = (
        "question",
        "answer",
    )

    list_filter = (
        "is_active",
    )

    ordering = (
        "order",
    )