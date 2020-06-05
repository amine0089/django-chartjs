from django.db import models

class Programing(models.Model):
	name = models.CharField(max_length=50)
	number = models.IntegerField()

	def __str__(self):
		return self.name
