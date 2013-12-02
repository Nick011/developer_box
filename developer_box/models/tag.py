from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
	title = models.CharField(max_length=20, blank=False, null=False)
	created_at = models.DateTimeField(auto_now_add=True)
	last_used_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		app_label = "developer_box"

	def __unicode__(self):
		return self.title