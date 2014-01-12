from django.db import models
from django.contrib.auth.models import User

class Bucket(models.Model):
	user = models.ForeignKey(User)
	title = models.CharField(blank=False, null=False, max_length=75)
	created_at = models.DateTimeField(auto_now=True)

	class Meta:
		app_label = "developer_box"

	def __unicode__(self):
		return self.title
