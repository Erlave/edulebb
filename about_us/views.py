from django.shortcuts import render
from django.views.generic import TemplateView
from .models import AboutPage,AboutCounter,AboutBanner,Testimonial

# Create your views here.


class AboutView(TemplateView):
    template_name = "about_us/about_us.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        about = AboutPage.objects.prefetch_related(
            "features",
            "benefits"
        ).first()

        context["about"] = about

        context["counters"] = AboutCounter.objects.all()

        context["banners"] = AboutBanner.objects.filter(
            is_active=True
        )

        context["testimonials"] = Testimonial.objects.filter(
            is_active=True
        )

        return context