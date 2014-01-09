from django.views.generic import ListView
from developer_box.models import Bucket, Item
from developer_box.mixins import LoginRequired

class DashboardView(LoginRequired, ListView):
	template_name = "toolbox/dashboard.html"
	context_object_name = "items"

	def get_queryset(self):
		self.buckets = Bucket.objects.filter(user=self.request.user)
		self.items = Item.objects.filter(bucket__id__in=self.buckets.values_list('id', flat=True))
		return self.items


	def get_context_data(self, **kwargs):
		context = super(DashboardView, self).get_context_data(**kwargs)
		context['buckets'] = self.buckets
		return context
