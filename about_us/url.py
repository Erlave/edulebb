from django.urls import path

from .views import AboutView,FAQView

urlpatterns = [
    path("",AboutView.as_view(),name="about"),
    path("faq/", FAQView.as_view(), name="faq"),
]