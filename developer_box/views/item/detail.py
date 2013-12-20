from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from developer_box.models import Item

class ItemDetailView(DetailView):
	template_name = "item/detail.html"
	context_object_name = "item"
	model = Item

	#def get_queryset(self):
		#return get_object_or_404(Item, slug=self.kwargs['slug'])

