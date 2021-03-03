from django.contrib import admin
from django.contrib.admin import ModelAdmin, register
from .models import *
from admin_auto_filters.filters import AutocompleteFilter
from django.utils.html import format_html


class CatagoryFilter(AutocompleteFilter):
    title = 'Category' # display title
    field_name = 'category' # name of the foreign key field

class SubCatagoryFilter(AutocompleteFilter):
    title = 'Subcatagory' # display title
    field_name = 'subcatagory'

class ProductInline(admin.TabularInline):
    model = AddDomesticItem

class ProductAdmin(admin.ModelAdmin):
    def delete (self, obj):
        return format_html(f'<input style="background-color:red;" onclick="{obj.pk}" type="button" value="Delete"/>')

    delete.allow_tags = True
    delete.short_description ='Delete Product'
    list_per_page = 10
    search_fields = ("sku","productname",)
    list_filter = [CatagoryFilter,SubCatagoryFilter]#("category","subcatagory",)
    list_display = ("sku","productname","category","subcatagory",'delete')
    inlines = [
        ProductInline,
    ]

class ProductInlineDomesticRaw(admin.TabularInline):
    model = AddDomesticRawItem


class ProductAdminDomesticRaw(admin.ModelAdmin):
    def delete (self, obj):
        return format_html(f'<input style="background-color:red;" onclick="{obj.pk}" type="button" value="Delete"/>')

    delete.allow_tags = True
    delete.short_description ='Delete Product'
    list_per_page = 10
    search_fields = ("sku","productname",)
    list_filter = [CatagoryFilter,SubCatagoryFilter]
    list_display = ("sku","productname","category","subcatagory",'delete')
    inlines = [
        ProductInlineDomesticRaw,
    ]

class ProductInlineImports(admin.TabularInline):
    model = AddImportsItem


class ProductAdminImports(admin.ModelAdmin):
    def delete (self, obj):
        return format_html(f'<input style="background-color:red;" onclick="{obj.pk}" type="button" value="Delete"/>')

    delete.allow_tags = True
    delete.short_description ='Delete Product'
    list_per_page = 10
    search_fields = ("sku","productname",)
    list_filter = [CatagoryFilter,SubCatagoryFilter]
    list_display = ("sku","productname","category","subcatagory",'delete')
    inlines = [
        ProductInlineImports,
    ] 

@admin.register(ProductOption)
class ProductOptionAdmin(admin.ModelAdmin):
    list_per_page = 10
    search_fields = ("sku","optionname",)
    list_display = ["optionname","optionvalue","sku","markuprate"]

@admin.register(AdditionalOption)
class AdditionalOptionAdmin(admin.ModelAdmin):
    list_per_page = 10
    search_fields = ("sku","optionname",)
    list_display = ["optionname","optionvalue","sku","markuprate"]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_per_page = 10
    search_fields = ("category",)
    list_display = ["category","region"]

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_per_page = 10
    search_fields = ("subcategory",)
    list_filter = ("region","category",)
    list_display = ["subcategory","category","region"]

@admin.register(SubSubCategory)
class SubSubCategoryAdmin(admin.ModelAdmin):
    list_per_page = 10
    search_fields = ("subsubcategory",)
    list_filter = ("region","category","subcategory",)
    list_display = ["subsubcategory","subcategory","category","region"]


admin.site.register(DomesticProduct,ProductAdmin)
admin.site.register(DomesticProductRaw,ProductAdminDomesticRaw)
admin.site.register(Region)
admin.site.register(ImportsProduct,ProductAdminImports)
admin.site.site_header = "Admin Dashboard"
admin.site.site_title = "Admin Dashboard"
admin.site.index_title = "Welcome to Admin Dashboard"