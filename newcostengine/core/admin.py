from django.contrib import admin
from .models import *


class ProductInline(admin.TabularInline):
    model = AddDomesticItem

class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductInline, 
    ]

class ProductInlineImports(admin.TabularInline):
    model = AddImportsItem

class ProductAdminImports(admin.ModelAdmin):
    inlines = [
        ProductInlineImports, 
    ]

admin.site.register(Product,ProductAdmin)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(SubSubCategory)
admin.site.register(ProductOption)
admin.site.register(Region)
admin.site.register(ImportsProduct,ProductAdminImports)
admin.site.site_header = "Admin Dashboard"
admin.site.site_title = "Admin Dashboard"
admin.site.index_title = "Welcome to Admin Dashboard"