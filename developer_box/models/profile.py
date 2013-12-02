from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.ForeignKey(User)
	#bio = models.TextField()
	#website = models.URLField()
	#github = models.URLField()
	#twitter = models.URLField()
	#linkedin = models.URLField()
	#stackoverflow = models.URLField()
	#image = models.ImageField(blank=True, null=True)
	#thumb = models.ImageField(blank=True, null=True)

	def __unicode__(self):
		return self.title
