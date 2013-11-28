from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.ForeignKey(User)
	#more to come

	def __unicode__(self):
		return self.title
