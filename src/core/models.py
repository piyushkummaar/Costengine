from django.db import models
from django.db.models.signals import m2m_changed
from adminsortable.models import SortableMixin

class Quantity(models.Model):
    quantity = models.IntegerField()

    class Meta:
        verbose_name = 'Quantity'
        verbose_name_plural = 'Quantities'
        db_table = 'tbl_qunatity' 
        ordering = ['quantity']

    def __unicode__(self):
        return self.quantity

class Price(models.Model):

    price = models.FloatField(help_text="Price in Dollar($).")

    class Meta:
        verbose_name = 'Price'
        verbose_name_plural = 'Prices'
        ordering = ['price']

    def __unicode__(self):
        return self.price

class Category(models.Model):
    category_resign = models.ForeignKey('Region',on_delete=models.CASCADE,blank=True,null=True)
    category_name = models.CharField(max_length=40)
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        db_table = 'tbl_category'
        managed = True

    def __str__(self):
        return self.category_name

class SubCategory(models.Model):
    category_resign = models.ForeignKey('Region',on_delete=models.CASCADE,blank=True,null=True)
    category_name = models.ForeignKey('Category',on_delete=models.CASCADE,blank=True,null=True)
    subcategory_name = models.CharField(max_length=40)
    
    class Meta:
        verbose_name = 'Sub Category'
        verbose_name_plural = 'Sub Categories'
        db_table = 'tbl_subcategory'
        managed = True
        

    def __str__(self):
        return self.subcategory_name

class SubSubCategory(models.Model):
    category_name = models.ForeignKey('Category',on_delete=models.CASCADE,blank=True,null=True)
    subcategory = models.ForeignKey('SubCategory',on_delete=models.CASCADE,blank=True,null=True)
    subsubcategory_name = models.CharField(max_length=40)
    class Meta:
        verbose_name = 'Sub Sub Category'
        verbose_name_plural = 'Sub Sub Categories'
        db_table = 'tbl_subsubcategory'
        managed = True
        

    def __str__(self):
        return self.subsubcategory_name

class Region(models.Model):
    region_name = models.CharField(max_length=40)
    
    class Meta:
        verbose_name = 'Region'
        verbose_name_plural = 'Regions'
        db_table = 'tbl_zone'
        managed = True

    def __str__(self):
        return self.region_name

class Product(models.Model):
    sku = models.CharField(max_length=120)
    product_name = models.CharField(max_length=250)
    region = models.ForeignKey('Region',on_delete=models.CASCADE,blank=True,null=True)
    category = models.ForeignKey('Category',on_delete=models.CASCADE,blank=True,null=True)
    subcategory = models.ForeignKey('SubCategory',on_delete=models.CASCADE,blank=True,null=True)
    subSubcategory = models.ForeignKey('SubSubCategory',on_delete=models.CASCADE,blank=True,null=True)
    quantities = models.ManyToManyField(Quantity)
    price = models.ManyToManyField(Price)
    markup = models.CharField(max_length=250, blank=True, null=True,help_text="Mark Up Value in Dollar($).")

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        db_table = 'tbl_product'
        managed = True

    def __str__(self):
        return self.product_name


class ProductOption(models.Model):
    product = models.ForeignKey('Product',  on_delete=models.CASCADE)
    option_name = models.CharField(max_length=250, blank=True, null=True)
    option_value = models.FloatField(blank=True, null=True)
    
    class Meta:
        verbose_name = 'Product Option'
        verbose_name_plural = 'Product Options'
        db_table = 'tbl_productoption'
        managed = True

    def __str__(self):
        return self.option_name

class New_Cost(models.Model):
    pro_cost_data = models.CharField(max_length=250, blank=True, null=True)
    
    def __str__(self):
        return self.pro_cost_data

class ProductCost(models.Model):
    product_cost = models.CharField(max_length=250, blank=True, null=True)
    product_cost_cal = models.ManyToManyField(New_Cost)
    
    class Meta:
        verbose_name = 'Product Cost'
        verbose_name_plural = 'Product Costs'
        db_table = 'tbl_productcost'
        managed = True

    def __str__(self):
        return self.product_cost


      
    


