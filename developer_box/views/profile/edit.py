from django.views.generic import UpdateView
from developer_box.models import Profile, Item, Follower
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, redirect
from developer_box.mixins import LoginRequired
from django import forms


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)

class ProfileEditView(LoginRequired, UpdateView):
	template_name = "profile/edit.html"
	context_object_name = "profile"
	model = Profile
	form_class = ProfileForm

	def get_object(self):
		return Profile.objects.get_or_create(user=self.request.user)[0]

	def get_context_data(self, **kwargs):
		user = self.request.user
		context = super(ProfileEditView, self).get_context_data(**kwargs)
		context['user_items'] = Item.objects.filter(user=user)
		context['buckets'] = user.bucket_set.all()
		context['recently_created'] = Item.objects.order_by('created_at').select_related('tag')[:20]
		context['follower_count'] = Follower.objects.filter(user=user).count()
		context['following_count'] = Follower.objects.filter(following=user).count()
		return context

	def form_valid(self, form):
		profile = form.save()
		profile.user = self.request.user
		profile.save()
		return redirect(reverse('profile-edit'))

