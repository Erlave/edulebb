from django.contrib import admin

from .models import (
    SiteSetting,
    FooterBox,
    FooterLink
)


class FooterLinkInline(admin.TabularInline):
    model = FooterLink
    extra = 1


@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):

    fieldsets = (
        ("Header", {
            "fields": (
                "site_name",
                "logo",
                "favicon",
            )
        }),

        ("Hero Section", {
            "fields": (
                "hero_title",
                "hero_description",
                "hero_image",
            )
        }),

        ("Footer", {
            "fields": (
                "footer_description",
                "copyright",
            )
        }),

        ("Contact", {
            "fields": (
                "address",
                "phone",
                "email",
            )
        }),

        ("Social Media", {
            "fields": (
                "facebook",
                "twitter",
                "instagram",
                "linkedin",
            )
        }),

        ("SEO", {
            "fields": (
                "meta_description",
            )
        }),

        ("Status", {
            "fields": (
                "is_active",
            )
        }),

    )

    def has_add_permission(self, request):
        return not SiteSetting.objects.exists()


@admin.register(FooterBox)
class FooterBoxAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "order",
    )

    list_editable = (
        "order",
    )

    inlines = [
        FooterLinkInline
    ]


@admin.register(FooterLink)
class FooterLinkAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "footer_box",
        "order",
    )

    list_filter = (
        "footer_box",
    )

    list_editable = (
        "order",
    )

    search_fields = (
        "title",
    )