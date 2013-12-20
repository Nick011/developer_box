from django.views.generic import ListView
from developer_box.models import Item

class ItemListView(ListView):
	template_name = "item/list.html"
	context_object_name = "item_list"
	model = Item
