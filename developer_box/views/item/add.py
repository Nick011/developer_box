from developer_box.models import Bucket, Item
from django.views.generic import View
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from developer_box.mixins import LoginRequired

class ItemAddView(LoginRequired, View):
	def post(self, request):
		bucket =	Bucket.objects.get(id=request.POST.get('bucket_id'))
		item = Item.objects.get(id=request.POST.get('item_id'))
		bucket.item_set.add(item)
		bucket.save()
		return redirect(reverse('item-detail', kwargs={'pk': item.id, 'slug': item.slug}))
