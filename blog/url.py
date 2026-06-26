from django.urls import path

from .views import BlogListView, BlogDetailView

urlpatterns = [

    path("list/",BlogListView.as_view(), name="blog_list"),

    path("details/<slug:slug>/", BlogDetailView.as_view(), name="blog_detail"),

]