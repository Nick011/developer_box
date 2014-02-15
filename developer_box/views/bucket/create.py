from developer_box.models import Bucket
from django.views.generic import View
from django.core.urlresolvers import reverse
from django.shortcuts import redirect

class BucketCreateView(View):
	def post(self, request):
		user = request.user
		Bucket.objects.create(title=request.POST.get('name'), user=user)
		return redirect(reverse('profile-detail', kwargs={'username': user.username}))
