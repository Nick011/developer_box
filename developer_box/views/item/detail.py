from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from developer_box.models import Item

class ItemDetailView(DetailView):
	template_name = "item/detail.html"
	context_object_name = "item"
	model = Item
	queryset = Item.objects.select_related()

	def get_context_data(self, **kwargs):
		context = super(ItemDetailView, self).get_context_data(**kwargs)
		context['item'].in_box = context['item'].in_box(self.request.user)
		context['similar_results'] = Item.objects.order_by('created_at')[:5]
		context['profile'] = context['item'].user.profile
		return context

