from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Course ,Review,Category
from .forms import ReviewForm
from django.shortcuts import redirect
from django.db.models import Q


class CourseListView(ListView):
    model = Course
    template_name = "course/course_list.html"
    context_object_name = "courses"
    

    def get_queryset(self):
        queryset = (
            Course.objects
            .filter(is_active=True)
            .select_related("category", "instructor")
            .order_by("-created_at")
        )

        search = self.request.GET.get("search")

        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) |
                Q(short_description__icontains=search)
            )

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search"] = self.request.GET.get("search", "")
        return context


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
            .prefetch_related("reviews")
        )

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["form"] = ReviewForm()

        context["related_courses"] = (
            Course.objects
            .filter(
                category=self.object.category,
                is_active=True
            )
            .exclude(id=self.object.id)[:3]
        )

        context["reviews"] = Review.objects.filter(is_active=True)

        # ✔️ ALL categories + 3 PRODUCTS per category
        categories = Category.objects.all()

        for category in categories:
            category.limited_products = (
                Course.objects
                .filter(
                    category=category,
                    is_active=True
                )
                [:3]
            )
        # related_products = Course.objects.filter(category=Course.category).exclude(id=Course.id)[:6]
        # context["related_products"] = related_products
        context["categories"] = categories
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        form = ReviewForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.course = self.object
            review.save()

            return redirect(
                "course-details",
                slug=self.object.slug
            )

        context = self.get_context_data()
        context["form"] = form
        return self.render_to_response(context)