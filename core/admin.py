from django.contrib import admin
from django.contrib.admin import ModelAdmin, register
from .models import *
from admin_auto_filters.filters import AutocompleteFilter
from django.utils.html import format_html
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter
from search_admin_autocomplete.admin import SearchAutoCompleteAdmin
#for import export functionality
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class MyModelAdmin(SearchAutoCompleteAdmin):
    ''' Search field on admin'''
    search_fields = ["search_field",]

class CatagoryFilter(AutocompleteFilter):
    ''' Autofield on Category '''
    title = 'Category' # display title
    field_name = 'category' # name of the foreign key field

class SubCatagoryFilter(AutocompleteFilter):
    ''' Autofield on Subcategory '''
    
    title = 'Subcatagory' # display title
    field_name = 'subcatagory'

'''
DOMESTIC
'''
class ProductInline(admin.TabularInline):
    model = AddDomesticItem

class ProductAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    def delete (self, obj):
        return format_html('<input type="button" style="background-color:#ba2121;" value="Delete" onclick="location.href=\'{0}/delete/\'" />'.format(obj.pk))

    delete.allow_tags = True
    delete.short_description ='Delete Product'
    list_per_page = 10
    search_fields = ("sku","productname")
    list_filter = (CatagoryFilter,SubCatagoryFilter,
        ('created_at', DateRangeFilter), ('updated_at', DateTimeRangeFilter),
    )
    list_display = ("sku","productname","category","subcatagory",'delete')
    inlines = [
        ProductInline,
    ]
    
'''
DOMESTIC SIZE 
'''
class ProductInlineSize(admin.TabularInline):
    model = AddDomesticSizeItem

class ProductAdminSize(ImportExportModelAdmin,admin.ModelAdmin):
    def delete (self, obj):
        return format_html('<input type="button" style="background-color:#ba2121;" value="Delete" onclick="location.href=\'{0}/delete/\'" />'.format(obj.pk))

    delete.allow_tags = True
    delete.short_description ='Delete Product'
    list_per_page = 10
    search_fields = ("sku","productname")
    list_filter = (CatagoryFilter,SubCatagoryFilter,
        ('created_at', DateRangeFilter), ('updated_at', DateTimeRangeFilter),
    )
    list_display = ("sku","productname","category","subcatagory",'delete')
    inlines = [
        ProductInlineSize,
    ]


'''
DOMESTIC RAW
'''
class ProductInlineDomesticRaw(admin.TabularInline):
    model = AddDomesticRawItem


class ProductAdminDomesticRaw(ImportExportModelAdmin,admin.ModelAdmin):
    def delete (self, obj):
        return format_html('<input type="button" style="background-color:#ba2121;" value="Delete" onclick="location.href=\'{0}/delete/\'" />'.format(obj.pk))

    delete.allow_tags = True
    delete.short_description ='Delete Product'
    list_per_page = 10
    search_fields = ("sku","productname",)
    # fields = [("sku","productname"),"region","category","subcatagory","subsubcategory",
    # ("markup","duty","exchage","broker"),"freight",("firstcost","printval"),("transfer","packing"),"overhead"]
    list_filter = (CatagoryFilter,SubCatagoryFilter,
        ('created_at', DateRangeFilter), ('updated_at', DateTimeRangeFilter),
    )
    list_display = ("sku","productname","category","subcatagory",'delete')
    inlines = [
        ProductInlineDomesticRaw,
    ]

'''
IMPORT

'''
class ProductInlineImports(admin.TabularInline):
    model = AddImportsItem
    
class ProductAdminImports(ImportExportModelAdmin,admin.ModelAdmin):
    def delete (self, obj):
        return format_html('<input type="button" style="background-color:#ba2121;" value="Delete" onclick="location.href=\'{0}/delete/\'" />'.format(obj.pk))

    delete.allow_tags = True
    delete.short_description ='Delete Product'
    list_per_page = 10
    search_fields = ("sku","productname",)
    list_filter = (CatagoryFilter,SubCatagoryFilter,
        ('created_at', DateRangeFilter), ('updated_at', DateTimeRangeFilter),
    )
    list_display = ("sku","productname","category","subcatagory",'delete')
    inlines = [
        ProductInlineImports,
    ] 

'''
FILTER's
'''
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
# admin.site.register(DomesticSizeProduct,ProductAdminSize)
admin.site.register(DomesticProductRaw,ProductAdminDomesticRaw)
admin.site.register(Region)
admin.site.register(ImportsProduct,ProductAdminImports)
admin.site.site_header = "Admin Dashboard"
admin.site.site_title = "Admin Dashboard"
admin.site.index_title = "Welcome to Admin Dashboard"