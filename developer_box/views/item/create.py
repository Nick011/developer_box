from django.views.generic.edit import CreateView
from django.shortcuts import redirect
from developer_box.models import Item
from developer_box.mixins import LoginRequired

class ItemCreateView(LoginRequired, CreateView):
	template_name = 'item/create.html'
	model = Item
	exclude = ['user', 'slug']

	def get_context_data(self, **kwargs):
		context = super(ItemCreateView, self).get_context_data(**kwargs)
		context['recently_created'] = self.model.objects.order_by('created_at')[:5]
		context['similar_results'] = context['recently_created']
		return context

	def form_valid(self, form):
		item = form.save()
		item.user = self.request.user
		item.save()
		return redirect(item.get_url())

