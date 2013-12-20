from django.views.generic.edit import CreateView
from developer_box.models import Item

class ItemCreateView(CreateView):
	template_name = 'item/create.html'
	model = Item
	success_url = '/'
