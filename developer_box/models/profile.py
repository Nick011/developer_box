from django.db import models
from django.contrib.auth.models import User
from follower import Follower

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

	def is_follower(self, current_user):
		return Follower.objects.filter(user=current_user, following=self.user).count()

	def buckets(self):
		return self.user.bucket_set.all()

	def following_count(self):
		return Follower.objects.filter(user=self.user).count()

	def follower_count(self):
		return Follower.objects.filter(following=self.user).count()
