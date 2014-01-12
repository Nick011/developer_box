from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.OneToOneField(User)
	bio = models.TextField(blank=True, null=True)
	website = models.URLField(blank=True, null=True)
	github = models.URLField(blank=True, null=True)
	twitter = models.URLField(blank=True, null=True)
	linkedin = models.URLField(blank=True, null=True)
	stackoverflow = models.URLField(blank=True, null=True)
	google = models.URLField(blank=True, null=True)
	facebook = models.URLField(blank=True, null=True)
	#image = models.ImageField(blank=True, null=True)
	#thumb = models.ImageField(blank=True, null=True)

	class Meta:
		app_label = "developer_box"

	def __unicode__(self):
		return self.user.username
