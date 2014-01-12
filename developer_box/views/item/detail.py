from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from developer_box.models import Item

class ItemDetailView(DetailView):
	template_name = "item/detail.html"
	context_object_name = "item"
	model = Item
	queryset = Item.objects.select_related()

	#def get_queryset(self):
		#return get_object_or_404(self.model.objects, pk=self.kwargs['id'])

