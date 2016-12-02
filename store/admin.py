from django.contrib import admin

from store.models import Product, UserProfile, MoneyRequest, Transaction


# Register your models here.
admin.site.register(Product)
admin.site.register(UserProfile)
admin.site.register(MoneyRequest)
admin.site.register(Transaction)