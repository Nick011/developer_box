from django.views.generic import DetailView
from developer_box.models import Profile
from django.shortcuts import get_object_or_404

class ProfileDetailView(DetailView):
	template_name = "profile/detail.html"
	context_object_name = "profile"
	model = Profile

	def get_object(self):
		return get_object_or_404(Profile.objects.select_related(), user__username=self.kwargs['slug'])
