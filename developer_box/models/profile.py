from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.OneToOneField(User)
	bio = models.TextField(blank=False, null=False)
	website = models.URLField(blank=False, null=False)
	github = models.URLField(blank=False, null=False)
	twitter = models.URLField(blank=False, null=False)
	linkedin = models.URLField(blank=False, null=False)
	stackoverflow = models.URLField(blank=False, null=False)
	#image = models.ImageField(blank=True, null=True)
	#thumb = models.ImageField(blank=True, null=True)

	class Meta:
		app_label = "developer_box"

	def __unicode__(self):
		return self.user.username
