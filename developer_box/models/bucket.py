from django.db import models
from django.contrib.auth.models import User
from item import Item

class Bucket(models.Model):
	user = models.ForeignKey(User)
	item = models.ManyToManyField(Item)
	title = models.CharField(blank=False, null=False, max_length=75)
	created_at = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.title
