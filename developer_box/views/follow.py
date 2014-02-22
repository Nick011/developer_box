from django.views.generic import View
from developer_box.models import Follower
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from developer_box.mixins import LoginRequired

class FollowAddView(LoginRequired, View):
	def get(self, request):
		follower = Follower.objects.create(user=request.user, following=request.POST.get('uid'))
		follower.save()
		return redirect(reverse('profile-detail', kwargs={'username': follower.following}))

	def get_context_data(self, **kwargs):
		bucket_slug = self.kwargs.get('bucket_slug', None)
		context = super(ProfileDetailView, self).get_context_data(**kwargs)
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