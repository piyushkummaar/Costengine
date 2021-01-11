from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Quantity(models.Model):
    qunanity = models.CharField(max_length=500,blank=True, null=True) 

    class Meta:
        verbose_name = 'Quantity'
        verbose_name_plural = 'Quantities'
        db_table = 'tbl_quantity'
        managed = True
    def __str__(self):
        return self.qunanity

class Price(models.Model):
    price = models.FloatField(blank=True,null=True)

    class Meta:
        verbose_name = 'Price'
        verbose_name_plural = 'Prices'
        db_table = 'tbl_price'
        managed = True

    def __unicode__(self):
        return f'{self.price}'

class Product(models.Model):
    sku = models.CharField(max_length=120)
    product_name = models.CharField(max_length=250)
    region = models.CharField(max_length=250)
    category = models.CharField(max_length=250)
    subcategory = models.CharField(max_length=250,blank=True, null=True)
    subSubcategory = models.CharField(max_length=250,blank=True, null=True)
    quantities = models.ManyToManyField(Quantity)
    price = models.ManyToManyField(Price)
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        db_table = 'tbl_product'
        managed = True

    def __str__(self):
        return self.product_name
    
class NewCost(models.Model):
    new_cost = models.FloatField(blank=True,null=True)


class ProductCost(models.Model):
    sku_number = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_cost = models.FloatField(blank=True,null=True)
    get_product_cost = models.ManyToManyField(Price)

    class Meta:
        verbose_name = 'Product Cost'
        verbose_name_plural = 'Product Costs'
        db_table = 'tbl_productCost'
        managed = True

    def save(self, *args, **kwargs):
        
        for i in self.get_product_cost.all():
            new = i.price + self.product_cost
            print(round(new, 2))
            # NewCost.objects.create(round(new, 2)) 
        super(ProductCost, self).save(*args, **kwargs) 
