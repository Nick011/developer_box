from django.shortcuts import get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.views.generic.base import RedirectView

class IndexView(RedirectView):
	permanent = False

	def get_redirect_url(self):
		current_user = self.request.user
		username = self.kwargs.get('username', None)
		if username:
			user = get_object_or_404(Profile.objects.select_related(), user__username=username)
			return reverse('profile-detail', kwargs={"username":user.username})
		elif current_user.is_authenticated():
			return reverse('profile-detail', kwargs={"username":current_user.username})
		else:
			return reverse('item-list')
