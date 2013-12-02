from django.db import models
from django.contrib.auth.models import User
from tag import Tag

class Item(models.Model):
	user = models.ForeignKey(User)
	tag = models.ManyToManyField(Tag)
	title = models.CharField(max_length=75, blank=False, null=False)
	body = models.TextField(blank=False, null=False)
	script = models.TextField(blank=False, null=False)
	slug = models.SlugField(unique=True, blank=False, null=False)
	created_at = models.DateTimeField(auto_now_add=True)
	last_updated_at = models.DateTimeField(auto_now=True, auto_now_add=True)
	last_viewed_at = models.DateTimeField(auto_now=True, auto_now_add=True)

	class Meta:
		app_label = "developer_box"

	def __unicode__(self):
		return self.title
