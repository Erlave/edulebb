from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Course



class CourseListView(ListView):
    model = Course
    template_name = "course/course_list.html"
    context_object_name = "courses"
    

    def get_queryset(self):
        return (
            Course.objects
            .filter(is_active=True)
            .select_related("category", "instructor")
            .order_by("-created_at")
        )


class CourseDetailView(DetailView):
    model = Course
    template_name = "course/course_details.html"
    context_object_name = "course"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_queryset(self):
        return (
            Course.objects
            .filter(is_active=True)
            .select_related("category", "instructor")
            # .prefetch_related("reviews")
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["related_courses"] = (
            Course.objects
            .filter(
                category=self.object.category,
                is_active=True
            )
            .exclude(id=self.object.id)[:3]
        )

        return context