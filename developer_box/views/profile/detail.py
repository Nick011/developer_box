from django.views.generic import DetailView
from developer_box.models import Profile, Item, Follower
from django.shortcuts import get_object_or_404

class ProfileDetailView(DetailView):
	template_name = 'profile/detail.html'
	context_object_name = 'profile'
	model = Profile

	def get_object(self):
		username = self.kwargs['username'] or self.request.user.username
		return get_object_or_404(Profile.objects.select_related(), user__username=username)

	def get_context_data(self, **kwargs):
		#user = self.request.user
		context = super(ProfileDetailView, self).get_context_data(**kwargs)
		user = context['profile'].user
		context['user_items'] = user.item_set.all()
		context['buckets'] = user.bucket_set.all()
		context['recently_created'] = Item.objects.order_by('created_at').select_related('tag')[:20]
		context['follower_count'] = Follower.objects.filter(user=user).count()
		context['following_count'] = Follower.objects.filter(following=user).count()
		return context
