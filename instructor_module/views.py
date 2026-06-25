from django.shortcuts import render
from django.views.generic import ListView
from .models import Instructor
from django.views.generic import DetailView

# Create your views here.





class InstructorListView(ListView):
    model = Instructor
    template_name = "instructor_module/Instructor_list.html"
    context_object_name = "Instructor"


class InstructorDetailView(DetailView):
    model = Instructor
    template_name = "instructor_module/Instructor_detail.html"
    context_object_name = "Instructor"
    slug_field = "slug"
    slug_url_kwarg = "slug"