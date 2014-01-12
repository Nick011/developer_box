from django.db import models
from django.contrib.auth.models import User

class Follower(models.Model):
	user = models.ForeignKey(User)
	following = models.ForeignKey(User)

