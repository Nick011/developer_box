from django.views.generic import ListView
from developer_box.models import Item

class ItemListView(ListView):
	template_name = "items/list.html"
	context_object_name = "item_list"
	model = Item

