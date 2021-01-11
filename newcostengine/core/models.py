from django.db import models

class Region(models.Model):
    region = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.region

    class Meta:
        verbose_name = 'Region'
        verbose_name_plural = 'Regions'
        db_table = 'tbl_region'
        managed = True

class Category(models.Model):
    region =  models.ForeignKey(Region, on_delete=models.CASCADE)
    category = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        db_table = 'tbl_categories'
        managed = True
    
class SubCategory(models.Model):
    region =  models.ForeignKey(Region, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.subcategory

    class Meta:
        verbose_name = 'SubCategory'
        verbose_name_plural = 'SubCategories'
        db_table = 'tbl_subcategories'
        managed = True

class SubSubCategory(models.Model):
    region =  models.ForeignKey(Region, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    subsubcategory = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.subsubcategory

    class Meta:
        verbose_name = 'SubSubCategory'
        verbose_name_plural = 'SubSubCategories'
        db_table = 'tbl_subsubcategories'
        managed = True

class Product(models.Model):
    sku = models.CharField(max_length=250, blank=True, null=True)
    region =  models.ForeignKey(Region, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcatagory = models.ForeignKey(SubCategory, on_delete=models.CASCADE,blank=True, null=True)
    subsubcategory = models.ForeignKey(SubSubCategory, on_delete=models.CASCADE,blank=True, null=True)
    productname = models.CharField(max_length=250, blank=True, null=True)
    markup = models.IntegerField(verbose_name ='Mark Up(in %)',default = 35,blank=True, null=True)
    productcostc = models.FloatField(default = 0.494,verbose_name = "Product Cost C$",null=True,blank=True)
    targetgrossprofit = models.FloatField(default = 33,verbose_name = "Target Gross Profit (in %)",null=True,blank=True)
    
    def __str__(self):
        return self.sku

    class Meta:
        verbose_name = 'Domestic Product'
        verbose_name_plural = 'Domestic Products'
        db_table = 'tbl_dproduct'
        managed = True

class AddDomesticItem(models.Model):
   product = models.ForeignKey(Product, on_delete=models.CASCADE)
   quantity = models.IntegerField()
   price = models.FloatField()
   productcost = models.FloatField(verbose_name = "Product Cost C$",null=True,blank=True)
   baseproductsalesprice = models.FloatField(verbose_name = "Base Product Sales Price C$",null=True,blank=True)
   
   def save(self, *args, **kwargs):
        data = Product.objects.all()
        for i in data:
            if i.productcostc :
                productcost = self.price + i.productcostc 
                self.productcost = round(productcost, 2)
            if i.targetgrossprofit:
                Baseproductsalesprice = self.productcost * ( 1 - (i.targetgrossprofit/100) ) 
                self.baseproductsalesprice = round(Baseproductsalesprice, 2)
                # print(Baseproductsalesprice)
        super(AddDomesticItem, self).save(*args, **kwargs)
   class Meta:
        verbose_name = 'Domestic Item'
        verbose_name_plural = 'Domestic Items'
        db_table = 'tbl_domesticitems'
        managed = True


class ImportsProduct(models.Model):
    sku = models.CharField(max_length=250, blank=True, null=True)
    region =  models.ForeignKey(Region, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcatagory = models.ForeignKey(SubCategory, on_delete=models.CASCADE,blank=True, null=True)
    subsubcategory = models.ForeignKey(SubSubCategory, on_delete=models.CASCADE,blank=True, null=True)
    productname = models.CharField(max_length=250, blank=True, null=True)
    setupfee = models.IntegerField(blank=True, null=True)
    markuprate = models.IntegerField(verbose_name ='Mark Up Rate(in %)',default = 35,blank=True, null=True)
    productcostu = models.FloatField(verbose_name = "Product Cost U$",null=True,blank=True)
    targetgrossprofit = models.FloatField(verbose_name = "Target Gross Profit (in %)",null=True,blank=True)
    duty = models.IntegerField(verbose_name ="Duty (in %)",default = 18,null=True,blank=True)
    markup = models.IntegerField(verbose_name ="Markup (in %)",default = 15,null=True,blank=True)

    def __str__(self):
        return self.sku

    class Meta:
        verbose_name = 'Import Product'
        verbose_name_plural = 'Imports Products'
        db_table = 'tbl_iproduct'
        managed = True

class AddImportsItem(models.Model):
   product = models.ForeignKey(ImportsProduct, on_delete=models.CASCADE)
   quantity = models.IntegerField()
   price = models.FloatField()
   setupfee = models.FloatField(verbose_name = "Setup Fee",null=True,blank=True)
   productcost = models.FloatField(verbose_name = "Product Cost U$",null=True,blank=True)
   baseproductsalesprice = models.FloatField(verbose_name = "Base Product Sales Price U$",null=True,blank=True)
   duty = models.FloatField(verbose_name = "Duty (in %)",null=True,blank=True)
   markup = models.FloatField(verbose_name = "Markup",null=True,blank=True)
   netduty = models.FloatField(verbose_name = "Net Duty U$",null=True,blank=True)

   def save(self, *args, **kwargs):
        data = ImportsProduct.objects.all()
        for i in data:
            if i.setupfee :
                imsetupfee = i.setupfee/self.price  
                self.setupfee = round(imsetupfee, 2)
            if i.productcostu:
                self.productcost = self.price + i.setupfee
            if i.duty:
                self.duty = (i.duty/100) * self.productcost
            if i.markup:
                self.markup = self.duty * (i.markup/100)    
            if i.targetgrossprofit:
                Baseproductsalesprice = self.productcost * ( 1 - (i.targetgrossprofit/100) ) 
                self.baseproductsalesprice = round(Baseproductsalesprice, 2)
                # print(Baseproductsalesprice)
            self.netduty = self.duty + self.markup
             
        super(AddImportsItem, self).save(*args, **kwargs)

   class Meta:
        verbose_name = 'Imports Item'
        verbose_name_plural = 'Imports Items'
        db_table = 'tbl_importsitems'
        managed = True


class ProductOption(models.Model):
    sku =  models.CharField(max_length=250, blank=True, null=True)
    optionname = models.CharField(max_length=250, blank=True, null=True) 
    optionvalue = models.FloatField(blank=True, null=True)
    markup = models.IntegerField(default=35, blank=True, null=True)
    
    def __str__(self):
        return self.optionname

    class Meta:
        verbose_name = 'Products Options'
        verbose_name_plural = 'Products Options'
        db_table = 'tbl_productoption'
        managed = True
