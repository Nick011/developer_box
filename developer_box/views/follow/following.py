from django.views.generic import ListView
from developer_box.models import Follower, Item, Profile
from django.db.models import Count
from django.db.models import Q

#TODO: CONSOLIDATE FOLLOWERS AND FOLLOWING AND MAYBE PROFILE DETAIL
class FollowingView(ListView):
	template_name = 'follow/following.html'
	context_object_name = 'following_list'
	model = Follower
	paginate_by = 15

	def get_queryset(self):
		return Follower.objects.filter(user__username=self.kwargs.get('username', None))

	def get_context_data(self, **kwargs):
		bucket_slug = self.kwargs.get('bucket_slug', None)
		context = super(FollowingView, self).get_context_data(**kwargs)
		profile = Profile.objects.get(user__username=self.kwargs.get('username', None))

		context['profile'] = profile
		context['buckets'] = profile.buckets()
		context['is_following'] = profile.is_follower(self.request.user)
		return context
