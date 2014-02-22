from django.views.generic import DetailView
from developer_box.models import Profile, Item, Follower
from django.shortcuts import get_object_or_404
from django.db.models import Q

#TODO: CONSOLIDATE FOLLOWERS AND FOLLOWING AND MAYBE PROFILE DETAIL
class ProfileDetailView(DetailView):
	template_name = 'profile/detail.html'
	context_object_name = 'profile'
	model = Profile

	def get_object(self):
		username = self.kwargs.get('username', None)
		return get_object_or_404(Profile.objects.select_related(), user__username=username)

	def get_context_data(self, **kwargs):
		bucket_slug = self.kwargs.get('bucket_slug', None)
		context = super(ProfileDetailView, self).get_context_data(**kwargs)
		user = context['profile'].user
		query = self.request.GET.get('q', None)
		buckets = user.bucket_set.all()

		#user with multiple buckets of same slug needs to be handled here!
		#if search query param has been added use it
		if bucket_slug and query:
			context['user_items'] = Item.objects.filter(Q(title__contains=query) | Q(description__contains=query), bucket__user=user, bucket__slug=bucket_slug)
		elif query:
			context['user_items'] = Item.objects.filter(Q(title__contains=query) | Q(description__contains=query))
		elif bucket_slug:
			context['user_items'] = Item.objects.filter(bucket__slug=bucket_slug, bucket__user=user)
		else:
			context['user_items'] = Item.objects.filter(bucket__user=user)

		context['buckets'] = buckets
		context['recently_created'] = Item.objects.order_by('created_at').select_related('tag')[:20]
		context['follower_count'] = Follower.objects.filter(user=user).count()
		context['following_count'] = Follower.objects.filter(following=user).count()
		return context
