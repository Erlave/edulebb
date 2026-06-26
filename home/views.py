from django.shortcuts import render
from django.views.generic import TemplateView
from about_us.models import AboutPage,AboutCounter,AboutBanner,AboutFeature,Testimonial
from blog.models import Blog
from course_module.models import Course
from instructor_module.models import Instructor

# Create your views here.

class HomeView(TemplateView):

    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # About
        context["about"] = AboutPage.objects.first()

        context["about_features"] = AboutFeature.objects.all()

        context["about_banner"] = AboutBanner.objects.filter(
            is_active=True
        ).first()

        # Counters
        context["counters"] = AboutCounter.objects.all()

        # Courses
        context["courses"] = (
            Course.objects.filter(is_active=True)
            .select_related("instructor", "category")
            .order_by("-id")[:6]
        )

        # Instructors
        context["instructors"] = Instructor.objects.all()[:4]

        # Testimonials
        context["testimonials"] = Testimonial.objects.filter(
            is_active=True
        )[:6]

        # Blogs
        context["blogs"] = (
            Blog.objects.filter(is_active=True)
            .select_related("author", "category")
            .order_by("-created_at")[:3]
        )

        return context



def header_component(request):
    return render(request, 'header_component.html' )


def footer_component(request):
    return render(request, 'footer_component.html')