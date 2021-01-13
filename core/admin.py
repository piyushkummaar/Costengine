from django.contrib import admin
from django.contrib.admin import ModelAdmin, register
from .models import *


class ProductInline(admin.TabularInline):
    model = AddDomesticItem

class ProductAdmin(admin.ModelAdmin):
    search_fields = ("sku","productname",)
    list_filter = ("category","subcatagory",)
    list_display = ["sku","productname","category","subcatagory"]
    inlines = [
        ProductInline,
    ]

class ProductInlineImports(admin.TabularInline):
    model = AddImportsItem


class ProductAdminImports(admin.ModelAdmin):
    search_fields = ("sku","productname",)
    list_filter = ("category","subcatagory",)    
    list_display = ["sku","productname","category","subcatagory"]
    inlines = [
        ProductInlineImports,
    ]

@admin.register(ProductOption)
class ProductOptionAdmin(admin.ModelAdmin):
    search_fields = ("sku","optionname",)
    list_display = ["optionname","optionvalue","sku","markuprate"]

@admin.register(AdditionalOption)
class AdditionalOptionAdmin(admin.ModelAdmin):
    search_fields = ("sku","optionname",)
    list_display = ["optionname","optionvalue","sku","markuprate"]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ("category",)
    list_display = ["category","region"]

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    search_fields = ("subcategory",)
    list_filter = ("region","category",)  
    list_display = ["subcategory","category","region"]

@admin.register(SubSubCategory)
class SubSubCategoryAdmin(admin.ModelAdmin):
    search_fields = ("subsubcategory",)
    list_filter = ("region","category","subcategory",) 
    list_display = ["subsubcategory","subcategory","category","region"]

admin.site.register(DomesticProduct,ProductAdmin)
admin.site.register(Region)
admin.site.register(ImportsProduct,ProductAdminImports)
admin.site.site_header = "Admin Dashboard"
admin.site.site_title = "Admin Dashboard"
admin.site.index_title = "Welcome to Admin Dashboard"