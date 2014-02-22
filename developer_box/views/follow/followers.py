from django.views.generic import ListView
from developer_box.models import Follower, Item, Profile
from django.db.models import Count
from django.db.models import Q

#TODO: CONSOLIDATE FOLLOWERS AND FOLLOWING AND MAYBE PROFILE DETAIL
class FollowersView(ListView):
	template_name = 'follow/followers.html'
	context_object_name = 'follower_list'
	model = Follower
	paginate_by = 15

	def get_queryset(self):
		return Follower.objects.filter(user__username=self.kwargs.get('username', None))

	def get_context_data(self, **kwargs):
		bucket_slug = self.kwargs.get('bucket_slug', None)
		context = super(FollowersView, self).get_context_data(**kwargs)
		context['profile'] = Profile.objects.get(user__username=self.kwargs.get('username', None))
		user = context['profile'].user

		#user with multiple buckets of same slug needs to be handled here!
		if bucket_slug:
			context['user_items'] = Item.objects.filter(bucket__user=user, bucket__slug=bucket_slug)
		else:
			context['user_items'] = user.item_set.all()

		context['buckets'] = user.bucket_set.all()
		context['recently_created'] = Item.objects.order_by('created_at').select_related('tag')[:20]
		context['follower_count'] = Follower.objects.filter(user=user).count()
		context['following_count'] = Follower.objects.filter(following=user).count()
		return context
