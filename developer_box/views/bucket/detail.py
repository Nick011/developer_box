from django.views.generic import DetailView
from developer_box.models import Bucket, Item
from developer_box.mixins import LoginRequired

class BucketDetailView(DetailView):
	template_name = 'bucket/detail.html'
	context_object_name = 'bucket'
	model = Bucket
	queryset = Bucket.objects.select_related()

	#def get_queryset(self):
	#	return get_object_or_404(Bucket.objects.select_related(), slug=self.kwargs['slug'], user__username=self.kwargs['username'])

