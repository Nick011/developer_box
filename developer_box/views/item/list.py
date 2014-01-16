from django.views.generic import ListView
from developer_box.models import Item, Tag
from django.db.models import Count
from django.db.models import Q

class ItemListView(ListView):
	template_name = "item/list.html"
	context_object_name = "item_list"
	model = Item
	paginate_by = 15

	def get_queryset(self):
		query = self.request.GET.get('q', '')
		return Item.objects.filter(Q(title__contains=query) | Q(description__contains =query)) if query else Item.objects.all()

	def get_context_data(self, **kwargs):
		context = super(ItemListView, self).get_context_data(**kwargs)
		context['tag_list'] = Tag.objects.annotate(Count('item'))
		return context
