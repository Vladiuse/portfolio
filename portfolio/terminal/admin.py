from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Directory, Image, Poll

admin.site.register(Directory, MPTTModelAdmin)
admin.site.register(Image)
admin.site.register(Poll)
