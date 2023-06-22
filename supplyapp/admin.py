from django.contrib import admin
from .models import *

# Register your models here.



admin.site.register(shopregmodel)
admin.site.register(regmodel)
admin.site.register(productmodel)
admin.site.register(buymodel)
admin.site.register(feedmodel)

admin.site.register(cartmodel)
admin.site.register(wishlistmodel)