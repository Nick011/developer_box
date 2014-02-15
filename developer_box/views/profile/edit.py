from django.views.generic import UpdateView
from developer_box.models import Profile, Item, Follower
from django.shortcuts import get_object_or_404

class ProfileEditView(UpdateView):
	template_name = "profile/edit.html"
	context_object_name = "profile"
	model = Profile

	def get_object(self):
		username = self.request.user.username
		return get_object_or_404(Profile.objects.select_related(), user__username=username)

	def get_context_data(self, **kwargs):
		user = self.request.user
		context = super(ProfileEditView, self).get_context_data(**kwargs)
		context['user_items'] = Item.objects.filter(user=user)
		context['buckets'] = user.bucket_set.all()
		context['recently_created'] = Item.objects.order_by('created_at').select_related('tag')[:20]
		context['follower_count'] = Follower.objects.filter(user=user).count()
		context['following_count'] = Follower.objects.filter(following=user).count()
		return context
