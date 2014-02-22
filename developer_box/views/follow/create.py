from django.views.generic import View
from developer_box.models import Follower
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from developer_box.mixins import LoginRequired

class FollowAddView(LoginRequired, View):
	def post(self, request):
		follower = Follower.objects.create(user=request.user, following=request.POST.get('uid'))
		follower.save()
		return redirect(reverse('profile-detail', kwargs={'username': follower.following}))
