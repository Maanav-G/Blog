from __future__ import unicode_literals 

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
# MVC - model view controller

class Post(models.Model):
	title = models.CharField(max_length=120)
	content = models.TextField()
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)


#python 2
	def __unicode__(self):
		return self.title

#python 3
	def __str__(self):
		return self.title


	def get_absolute_url (self):
		return reverse("posts:detail", kwargs={"id": self.id})
		#return "/posts/%s/" %(self.id)