from django.conf.urls import patterns, include, url
from django.contrib import admin, auth
from views import *

admin.autodiscover()

urlpatterns = patterns('',
  # Examples:
  # url(r'^$', 'developer_box.views.home', name='home'),
  # url(r'^blog/', include('blog.urls')),
  url(r'^item/comments/', include('django.contrib.comments.urls')),

  url(r'^admin/', include(admin.site.urls)),
  url(r'^accounts/', include('registration.backends.default.urls')),
  
  #url(r'^$', IndexView.as_view(), name='home'),
  url(r'^$', ItemListView.as_view(), name='home'),
  
  #item actions
  #url(r'^search/$', ItemListView.as_view(), name='item-list'),
  url(r'^items/$', ItemListView.as_view(), name='item-list'),
  url(r'^item/create/$', ItemCreateView.as_view(), name='item-create'),
  url(r'^item/(?P<pk>\d+)/(?P<slug>[\w-]+)/$', ItemDetailView.as_view(), name='item-detail'),
  url(r'^item/add/$', ItemAddView.as_view(), name='item-add'),

  #url(r'^toolbox/create/$', ToolboxCreateView.as_view(), name='toolbox-create'),
  
  #user actions
  url(r'^accounts/profile/$', ProfileDetailView.as_view(), name='profile-edit'),
  url(r'^follow/$', FollowView.as_view(), name='follow'),

  url(r'^(?P<username>[\w-]+)/$', ProfileDetailView.as_view(), name='profile-detail')
)
