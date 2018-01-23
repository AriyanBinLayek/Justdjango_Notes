from django.db import models

# Create your models here.


class Entry(models.Model):
	title = models.CharField(max_length=120)
	description = models.TextField()

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return "/entries/{0}/".format(self.id)