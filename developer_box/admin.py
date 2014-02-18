from django.contrib import admin
from developer_box.models import *

admin.site.register(Bucket)
admin.site.register(Item)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Profile)
admin.site.register(Follower)

