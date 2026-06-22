from django.urls import path 
from . import views


urlpatterns = [
    path('list/' , views.CourseListView.as_view() , name='course_list'),
    path('course-details/<str:slug>', views.CourseDetailView.as_view() , name='course-details'),
]
