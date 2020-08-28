from django.db import models
# Create your models here.
# class TourInfo(models.Model):
	
class TourModel(models.Model):
	time = models.CharField(max_length = 20)
	dates = models.CharField(max_length = 50)
	venue = models.CharField(max_length = 50)
	band = models.CharField(max_length = 50)

	def __str__(self):
		return self.dates + self.venue

class StoryModel(models.Model):
	story_description = models.TextField()
	