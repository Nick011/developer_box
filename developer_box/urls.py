from django.conf.urls import patterns, include, url
from django.contrib import admin, auth
from views import *
from rest_api import *

from django.conf.urls import patterns, url, include
from rest_framework import routers


admin.autodiscover()

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('groups', GroupViewSet)
router.register('followers', FollowerViewSet)
router.register('buckets', BucketViewSet)
router.register('items', ItemViewSet)

urlpatterns = patterns('',
  #include api
  url(r'api/', include(router.urls)),

  # Examples:
  # url(r'^$', 'developer_box.views.home', name='home'),
  # url(r'^blog/', include('blog.urls')),
  url(r'^item/comments/', include('django.contrib.comments.urls')),

  #installed apps
  url(r'^admin/', include(admin.site.urls)),
  url(r'^accounts/', include('registration.backends.default.urls')),
  url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
  
  #begin code beaker urls
  url(r'^$', ProfileDetailView.as_view(), name='home'),
  #url(r'^$', ItemListView.as_view(), name='home'),
  
  #item actions
  #url(r'^search/$', ItemListView.as_view(), name='item-list'),
  url(r'^items/$', ItemListView.as_view(), name='item-list'),
  url(r'^item/create/$', ItemCreateView.as_view(), name='item-create'),
  url(r'^item/(?P<pk>\d+)/(?P<slug>[\w-]+)/$', ItemDetailView.as_view(), name='item-detail'),
  url(r'^item/add/$', ItemAddView.as_view(), name='item-add'),

  #bucket actions
  url(r'^bucket/create/$', BucketCreateView.as_view(), name='bucket-create'),

  #url(r'^toolbox/create/$', ToolboxCreateView.as_view(), name='toolbox-create'),
  
  #follower actions
  url(r'^follow/$', FollowAddView.as_view(), name='follow'),
  url(r'^(?P<username>[\w-]+)/followers/$', FollowersView.as_view(), name='followers'),
  url(r'^(?P<username>[\w-]+)/following/$', FollowingView.as_view(), name='following'),

  #profile actions
  url(r'^accounts/profile/$', ProfileEditView.as_view(), name='profile-edit'),
  url(r'^(?P<username>[\w-]+)/(?P<bucket_slug>[\w-]+)/$', ProfileDetailView.as_view(), name='profile-detail'),
  url(r'^(?P<username>[\w-]+)/$', ProfileDetailView.as_view(), name='profile-detail'),

)
