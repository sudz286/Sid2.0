from django.views.generic import TemplateView
from django.shortcuts import render


# Create your views here.
class HomePageView(TemplateView):
    template_name = "home.html"

class TourPageView(TemplateView):
    template_name = "tour.html"

class StoryPageView(TemplateView):
    template_name = "home.html"

class ContactPageView(TemplateView):
    template_name = "contact.html"


