from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from .forms import BlogCommentForm
from .models import Blog

# Create your views here.


class BlogListView(ListView):

    model = Blog

    template_name = "blog/blog_list.html"

    context_object_name = "blogs"

    

    queryset = Blog.objects.filter(
        is_active=True
    ).select_related(
        "category",
        "author",
    )


class BlogDetailView(DetailView):

    model = Blog

    template_name = "blog/blog_details.html"

    context_object_name = "blog"

    slug_field = "slug"

    slug_url_kwarg = "slug"

    queryset = Blog.objects.filter(
        is_active=True
    ).select_related(
        "category",
        "author",
    ).prefetch_related(
        "comments"
    )

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        blog = self.object

        context["form"] = BlogCommentForm()

        context["popular_posts"] = Blog.objects.filter(
            is_active=True
        ).exclude(
            id=blog.id
        ).order_by("-views")[:5]

        context["recent_posts"] = Blog.objects.filter(
            is_active=True
        ).exclude(
            id=blog.id
        )[:5]

        context["categories"] = (
            self.model.category.field.related_model.objects.all()
        )

        context["related_posts"] = Blog.objects.filter(
            category=blog.category,
            is_active=True
        ).exclude(
            id=blog.id
        )[:3]

        context["comments"] = blog.comments.filter(
            is_active=True
        )

        return context

    def post(self, request, *args, **kwargs):

        self.object = self.get_object()

        form = BlogCommentForm(request.POST)

        if form.is_valid():

            comment = form.save(commit=False)

            comment.blog = self.object

            comment.save()

            return redirect(self.object.get_absolute_url())

        context = self.get_context_data()

        context["form"] = form

        return self.render_to_response(context)