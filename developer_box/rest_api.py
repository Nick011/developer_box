from django.contrib.auth.models import User, Group
from models import *
from rest_framework import viewsets, routers

# TODO create a folder the api stuff

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
	model = User

class GroupViewSet(viewsets.ModelViewSet):
	model = Group

class FollowerViewSet(viewsets.ModelViewSet):
	model = Follower

class BucketViewSet(viewsets.ModelViewSet):
	model = Bucket

class ItemViewSet(viewsets.ModelViewSet):
	model = Item
