from django.views.generic import TemplateView, ListView
from django.shortcuts import render
from .models import TourModel

# Create your views here.
class HomePageView(TemplateView):
    template_name = "home.html"

class TourPageView(ListView):
    template_name = "tour.html"
    model = TourModel
    context_object_name = "tour_info"

class StoryPageView(TemplateView):
    template_name = "story.html"

class ContactPageView(TemplateView):
    template_name = "contact.html"


