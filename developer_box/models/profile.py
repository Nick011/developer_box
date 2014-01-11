from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.OneToOneField(User)
	bio = models.TextField(null=True)
	website = models.URLField(null=True)
	github = models.URLField(null=True)
	twitter = models.URLField(null=True)
	linkedin = models.URLField(null=True)
	stackoverflow = models.URLField(null=True)
	google = models.URLField(null=True)
	#image = models.ImageField(blank=True, null=True)
	#thumb = models.ImageField(blank=True, null=True)

	class Meta:
		app_label = "developer_box"

	def __unicode__(self):
		return self.user.username
