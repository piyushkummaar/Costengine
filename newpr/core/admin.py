from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Product)
admin.site.register(Quantity)
admin.site.register(Price)
admin.site.register(ProductCost)
admin.site.register(NewCost)