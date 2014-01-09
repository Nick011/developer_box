from django.views.generic.edit import CreateView
from developer_box.models import Item
from developer_box.mixins import LoginRequired

class ItemCreateView(LoginRequired, CreateView):
	template_name = 'item/create.html'
	model = Item
	success_url = '/'
