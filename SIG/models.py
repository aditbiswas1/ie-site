from django.db import models

# Create your models here.
class SIGroup(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	slug = models.SlugField()


	def __unicode__(self):
		return self.name