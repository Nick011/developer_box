from django.db import models
from django.contrib.auth.models import User

class Follower(models.Model):
	user = models.ForeignKey(User, related_name='follower')
	following = models.ForeignKey(User, related_name='followee')

	class Meta:
		app_label = "developer_box"
		verbose_name = "Followers"

	def __unicode__(self):
		return 'Followers'

