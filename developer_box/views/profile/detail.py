from django.views.generic import TemplateView
from developer_box.models import Profile
from django.shortcuts import render

class ProfileDetailView(TemplateView):
	template_name = "profile/detail.html"
	context_object_name = "profile"
	model = Profile

