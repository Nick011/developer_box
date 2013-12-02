from django.conf.urls import patterns, include, url
from django.contrib import admin, auth
from views import *


admin.autodiscover()

urlpatterns = patterns('',
  # Examples:
  # url(r'^$', 'developer_box.views.home', name='home'),
  # url(r'^blog/', include('blog.urls')),

  url(r'^admin/', include(admin.site.urls)),
  url(r'^accounts/', include('registration.backends.default.urls')),
  
  url(r'^$', IndexView.as_view()),
  url(r'^items/$', ItemListView.as_view(), name='item-list'),
  url(r'^item/(?P<slug>\w+)/$', ItemDetailView.as_view(), name='item-detail'),
)
