from django.views.generic.edit import FormView
from django import forms
from django.shortcuts import redirect
from django.core.urlresolvers import reverse_lazy
from developer_box.models import Item, Tag, Bucket
from developer_box.mixins import LoginRequired

class ItemCreateForm(forms.Form):
	title = forms.CharField()
	script = forms.CharField(widget=forms.Textarea)
	description = forms.CharField(widget=forms.Textarea)
	tags = forms.ModelChoiceField(queryset=Tag.objects.all(), empty_label=None)
	bucket = forms.ModelChoiceField(queryset=None, empty_label=None)

	def __init__(self, user, *args, **kwargs):
		super(ItemCreateForm, self).__init__(*args, **kwargs)
		self.fields['bucket'].queryset = Bucket.objects.filter(user=user)

	def __call__(self, *args, **kwargs):
		return self


class ItemCreateView(LoginRequired, FormView):
	template_name = 'item/create.html'

	def get_form_class(self):
		return ItemCreateForm(self.request.user)

	def form_valid(self, form):
		# This method is called when valid form data has been POSTed.
		# It should return an HttpResponse.
		print "VALID"
		item = Item(form)
		item.user = self.request.user
		if item.save(): return redirect(reverse('item-detail', kwargs={id: item.id, slug: item.slug}))

	def form_invalid(self, form):
		print "INVALID"
		print form.errors
		return self.render_to_response(self.get_context_data(form=form))
