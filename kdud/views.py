from django.views.generic import ListView
from django.shortcuts import render
from .models import TourModel

# Create your views here.
class HomePageView(ListView):
	template_name = "base.html"
	model = TourModel
	context_object_name = "tour_info"    


