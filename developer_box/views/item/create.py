from django.views.generic.edit import FormView, CreateView
from django import forms
from django.shortcuts import redirect
from developer_box.models import Item, Tag, Bucket
from developer_box.mixins import LoginRequired

class ItemCreateForm(forms.Form):
	title = forms.CharField()
	script = forms.CharField(widget=forms.Textarea)
	description = forms.CharField(widget=forms.Textarea)
	tag = forms.ModelChoiceField(queryset=Tag.objects.all(), empty_label=None)
	bucket = forms.ModelChoiceField(queryset=None, empty_label=None)

	def __init__(self, user, *args, **kwargs):
		super(ItemCreateForm, self).__init__(*args, **kwargs)
		self.fields['bucket'].queryset = Bucket.objects.filter(user=user)

	def __call__(self, *args, **kwargs):
		return self

'''
class ItemCreateView(LoginRequired, FormView):
	template_name = 'item/create.html'
	form_class = ItemCreateForm

	def get_form(self, form_class):
		return form_class(self.request.user, **self.get_form_kwargs())

	def form_valid(self, form):
		print form.cleaned_data
		item = Item.objects.create(**form.cleaned_data)
		item.user = self.request.user
		if item.save():
			return redirect(item.get_url())

	def form_invalid(self, form):
		return self.render_to_response(self.get_context_data(form=form))
'''

class ItemCreateView(LoginRequired, CreateView):
	template_name = 'item/create.html'
	model = Item
	fields = ['tag', 'bucket', 'title', 'description', 'script']

	def form_valid(self, form):
		item = form.save(commit=False)
		item.user = self.request.user
		item.save()
		return redirect(item.get_url())


