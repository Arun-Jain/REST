from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Casino(models.Model):
	name = models.CharField(max_length=50)
	address = models.CharField(max_length=250)
	created_at = models.DateTimeField(auto_now_add=True)
	modified_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name
