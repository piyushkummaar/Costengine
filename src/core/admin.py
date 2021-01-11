from django.contrib import admin
from .models import *

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('sku', 'product_name','region','category','subcategory')
    search_fields = ['sku','category']
    

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name','category_resign')
admin.site.register(Region)

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('subcategory_name','category_name','category_resign')

@admin.register(SubSubCategory)
class SubSubCategoryAdmin(admin.ModelAdmin):
    list_display = ('subsubcategory_name','subcategory','category_name')

admin.site.register(Quantity)
admin.site.register(Price)
admin.site.register(ProductCost)
admin.site.register(New_Cost)
admin.site.register(ProductOption)

admin.site.site_header = "Admin Dashboard"
admin.site.site_title = "Admin Dashboard"
admin.site.index_title = "Welcome to Admin Dashboard"
