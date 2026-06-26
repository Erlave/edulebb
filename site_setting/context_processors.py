from .models import SiteSetting, FooterBox


def site_setting(request):

    return {

        "site_setting":
            SiteSetting.objects.filter(
                is_active=True
            ).first(),

        "footer_boxes":
            FooterBox.objects.prefetch_related(
                "links"
            )

    }