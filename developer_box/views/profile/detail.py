from django.views.generic import DetailView
from developer_box.models import Profile, Item
from django.shortcuts import get_object_or_404

class ProfileDetailView(DetailView):
	template_name = "profile/detail.html"
	context_object_name = "profile"
	model = Profile

	def get_object(self):
		return get_object_or_404(Profile.objects.select_related(), user__username=self.kwargs['username'])

	def get_context_data(self, **kwargs):
		context = super(ProfileDetailView, self).get_context_data(**kwargs)
		context['user_items'] = Item.objects.filter(user=self.request.user)
		context['recently_created'] = Item.objects.order_by('created_at')[:20]
		return context
