from django.urls import path
from .views import HomePageView,TourPageView,ContactPageView,StoryPageView

urlpatterns = [
    path('',HomePageView.as_view(),name ="home"),
    path('story',StoryPageView.as_view(),name="story"),
    path('tour',TourPageView.as_view(),name="tour"),
    path('contact',ContactPageView.as_view(),name="contact")
]