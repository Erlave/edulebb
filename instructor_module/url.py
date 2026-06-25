from django.urls import path
from .views import InstructorListView, InstructorDetailView

urlpatterns = [
    path("list/", InstructorListView.as_view(), name="Instructor_list"),
    path("details/<slug:slug>/", InstructorDetailView.as_view(), name="Instructor_detail"),
]