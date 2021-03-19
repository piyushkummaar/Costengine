from django.db import models
from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver
import decimal
import math


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

class DomesticProduct(models.Model):
    sku = models.CharField(max_length=250, unique=True)
    region =  models.ForeignKey(Region, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcatagory = models.ForeignKey(SubCategory, on_delete=models.CASCADE,blank=True, null=True)
    subsubcategory = models.ForeignKey(SubSubCategory, on_delete=models.CASCADE,blank=True, null=True)
    productname = models.CharField(max_length=250)
    markup = models.IntegerField(verbose_name ='Mark Up Rate(in %)',default = 35,blank=True, null=True)
    productcostc = models.FloatField(default = 0.494,verbose_name = "Product Cost C$",null=True,blank=True)
    targetgrossprofit = models.IntegerField(default = 33,verbose_name = "Target Gross Profit (in %)",null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sku


    class Meta:
        verbose_name = 'Domestic Product'
        verbose_name_plural = 'Domestic Products'
        db_table = 'tbl_domesticproducts'
        managed = True

class AddDomesticItem(models.Model):
    product = models.ForeignKey(DomesticProduct, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField(null=True,blank=True) #models.DecimalField(max_digits=5, decimal_places=2)
    productcost = models.FloatField(verbose_name = "Product Cost C$",null=True,blank=True)#models.DecimalField(verbose_name = "Product Cost C$",max_digits=5, decimal_places=2,null=True,blank=True)
    baseproductsalesprice = models.FloatField(verbose_name = "Base Product Sales Price C$",null=True,blank=True)#models.DecimalField(verbose_name = "Base Product Sales Price C$",max_digits=5, decimal_places=2,null=True,blank=True)

    def save(self, *args, **kwargs):
        data = DomesticProduct.objects.all()
        productcost = ""
        targetgrossprofit = ""
        for i in data:
            if i.productcostc :
                productcost = i.productcostc
            if i.targetgrossprofit:
                targetgrossprofit =  i.targetgrossprofit
        self.productcost = round((self.price + productcost),2)
        self.baseproductsalesprice = round(self.productcost / ( 1 - (targetgrossprofit/100) ),2)
        super(AddDomesticItem, self).save(*args, **kwargs)


    class Meta:
        verbose_name = 'Domestic Item'
        verbose_name_plural = 'Domestic Items'
        db_table = 'tbl_domesticitems'
        managed = True


'''
    Domestic Raw products
'''

class DomesticProductRaw(models.Model):
    sku = models.CharField(max_length=250, unique=True)
    region =  models.ForeignKey(Region, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcatagory = models.ForeignKey(SubCategory, on_delete=models.CASCADE,blank=True, null=True)
    subsubcategory = models.ForeignKey(SubSubCategory, on_delete=models.CASCADE,blank=True, null=True)
    productname = models.CharField(max_length=250)
    markup = models.IntegerField(verbose_name ='Mark Up Rate(in %)',default = 35,blank=True, null=True)
    firstcost = models.FloatField(verbose_name = "1st Cost China US$",null=True,blank=True)
    exchage = models.IntegerField(verbose_name ='Exchange(in %)',default = 35,blank=True, null=True)
    duty = models.IntegerField(verbose_name ='Duty(in %)',default = 18,blank=True, null=True)
    broker = models.IntegerField(verbose_name ='Broker(in %)',default = 1,blank=True, null=True)
    printval = models.FloatField(verbose_name = "Print",null=True,blank=True)
    transfer = models.FloatField(verbose_name = "Transfer",null=True,blank=True)
    packing = models.FloatField(verbose_name = "Packing",null=True,blank=True)
    freight = models.IntegerField(verbose_name ='Freight(in %)',default = 10,blank=True, null=True)
    overhead = models.FloatField(verbose_name = "Overhead(in %)",default = 33,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sku


    class Meta:
        verbose_name = 'Domestic(Raw) Product'
        verbose_name_plural = 'Domestic(Raw) Products'
        db_table = 'tbl_domesticrawproducts'
        managed = True

class AddDomesticRawItem(models.Model):
    product = models.ForeignKey(DomesticProductRaw, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True,blank=True)
    marketval = models.FloatField(verbose_name = "Market Value",null=True,blank=True)
    distributorcost = models.FloatField(verbose_name = "Distributor Cost",null=True,blank=True)
    price = models.FloatField(verbose_name = "1st Cost",null=True,blank=True)
    totallandedcost = models.FloatField(verbose_name = "Total Landed Cost",null=True,blank=True)
    ldp = models.FloatField(verbose_name = "Landed Duty Paid",null=True,blank=True)
    printval = models.FloatField(verbose_name = "Print",null=True,blank=True)
    overhead = models.FloatField(verbose_name = "Overhead",null=True,blank=True)
    totalcost = models.FloatField(verbose_name = "Total Cost",null=True,blank=True)
    netsellprice = models.FloatField(verbose_name = "Net Sell Price",null=True,blank=True)
    markup = models.IntegerField(verbose_name = "Markup (in %)",null=True,blank=True)
    onnetsell = models.FloatField(verbose_name = "$$ On Net Sell Price",null=True,blank=True)
    marginonsell = models.IntegerField(null=True,blank=True)
    listprice = models.FloatField(verbose_name = "List price",null=True,blank=True)
    distributormargin = models.IntegerField(null=True,blank=True)
    distributor = models.FloatField(verbose_name = "Distributor $$",null=True,blank=True)


    def save(self, *args, **kwargs):
        data = DomesticProductRaw.objects.all()
        firstcost = ''
        exchange = ''
        duty = ''
        broker = ''
        freight = ''
        transfer = ''
        pval = '' #(Print Value)
        overhead = ''
        for i in data:
            if i.firstcost:
                firstcost = i.firstcost
            if i.exchage and i.duty and i.broker and i.freight and i.overhead:
                exchange = i.exchage/100
                duty = i.duty/100
                broker =  i.broker/100
                freight  = i.freight/100
                overhead = i.overhead/100
            if i.transfer and i.packing and i.printval:
                transfer = i.transfer
                packing =  i.packing
                pval = i.printval
        #1st Cost
        self.price = round((firstcost * self.quantity),2)
        #total Percentage
        self.totallandedcost =  round((exchange + duty + broker + freight),2)
        # landed duty paid
        self.ldp =  round((self.totallandedcost * firstcost ),2)
        #print
        self.printval = round((pval + transfer + packing),2)
        #overhead
        self.overhead = round(((self.ldp + self.printval)* overhead),2)
        #totalcost
        self.totalcost = round((self.ldp + self.printval + self.overhead),2)
        #net sell price
        if self.marketval:
            '''
                marketvalue is input value by user
            '''
            #Net Sell Price
            self.netsellprice = round((self.totalcost * self.marketval),2)
        if  self.netsellprice: 
            #On Net Sell
            self.onnetsell = round((self.netsellprice - self.totalcost),2)
            #MARKUP
            mark = (self.onnetsell / self.totalcost) * 100
            self.markup = math.ceil(mark)
            #MARGIN ON SELL
            margin = (self.onnetsell / self.netsellprice) * 100
            self.marginonsell = math.ceil(margin)
            #LIST PRICE
            # 1.666666666643
            self.listprice = round((self.netsellprice * self.distributorcost),2)
            #DISTRIBUTOR MARGIN
            distributor = ((self.listprice - self.netsellprice)/self.listprice) * 100
            self.distributormargin = math.ceil(distributor)
            # DISTRIBUTOR $$
            self.distributor = round((self.listprice - self.netsellprice),2)
        super(AddDomesticRawItem, self).save(*args, **kwargs)


    class Meta:
        verbose_name = 'Domestic Raw Item'
        verbose_name_plural = 'Domestic Raw Items'
        db_table = 'tbl_domesticrawitems'
        managed = True


'''
    Imports
'''
class ImportsProduct(models.Model):
    sku = models.CharField(max_length=250,unique=True)
    region =  models.ForeignKey(Region, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcatagory = models.ForeignKey(SubCategory, on_delete=models.CASCADE,blank=True, null=True)
    subsubcategory = models.ForeignKey(SubSubCategory, on_delete=models.CASCADE,blank=True, null=True)
    productname = models.CharField(max_length=250)
    setupfee = models.IntegerField(blank=True, null=True)
    markuprate = models.IntegerField(verbose_name ='Mark Up Rate(in %)',default = 35,blank=True, null=True)
    targetgrossprofit = models.IntegerField(verbose_name = "Target Gross Profit (in %)",null=True,blank=True)
    duty = models.IntegerField(verbose_name ="Duty (in %)",default = 18,null=True,blank=True)
    markup = models.IntegerField(verbose_name ="Markup (in %)",default = 15,null=True,blank=True)
    frieghtvalue = models.IntegerField(verbose_name ="FRIEGHT ADMIN/UNIT (in %)",default = 15,null=True,blank=True)
    forex = models.FloatField(verbose_name ="Forex",default = 1.35,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sku

    class Meta:
        verbose_name = 'Import Product'
        verbose_name_plural = 'Imports Products'
        db_table = 'tbl_importproducts'
        managed = True

class AddImportsItem(models.Model):
    product = models.ForeignKey(ImportsProduct, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    freight = models.FloatField(verbose_name = "Frieght UNIT",help_text="Enter the Freight values",null=True,blank=True)
    freightadmin = models.FloatField(verbose_name = "Frieght Admin/UNIT",help_text="Enter the Freight Admin values",null=True,blank=True)
    setupfee = models.FloatField(verbose_name = "Setup Fee",null=True,blank=True)
    productcost = models.FloatField(verbose_name = "Product Cost U$",null=True,blank=True)
    baseproductsalesprice = models.FloatField(verbose_name = "Base Product Sales Price U$",null=True,blank=True)
    totalfrieght = models.FloatField(verbose_name = "Total Frieght",null=True,blank=True)
    duty = models.FloatField(verbose_name = "Duty (in %)",null=True,blank=True)
    markup = models.FloatField(verbose_name = "Markup",null=True,blank=True)
    netduty = models.FloatField(verbose_name = "Net Duty U$",null=True,blank=True)
    subtotal = models.FloatField(verbose_name = "Sub Total",null=True,blank=True)
    forex = models.FloatField(verbose_name = "Forex",null=True,blank=True)

    def save(self, *args, **kwargs):
        data = ImportsProduct.objects.all()
        for i in data:
            if i.setupfee :
                imsetupfee = ((i.setupfee/self.quantity)/self.price)
                self.setupfee = round(imsetupfee, 2)
                self.productcost = round((self.price + (i.setupfee/self.quantity)),2)
            if i.duty:
                self.duty = round(((i.duty/100) * self.productcost),2)
            if i.markup:
                self.markup = round((self.duty * (i.markup/100)),2)
            if i.targetgrossprofit:
                Baseproductsalesprice = self.productcost / ( 1 - (i.targetgrossprofit/100) )
                self.baseproductsalesprice = round(Baseproductsalesprice, 2)
        super(AddImportsItem, self).save(*args, **kwargs)

    # @receiver(pre_save, sender=ImportsProduct)
    # def addvalues(sender,instance, **kwargs):
    #     data = ImportsProduct.objects.filter(sku=instance)
    #     for i in data:
    #         imdata = AddImportsItem.objects.filter(product_id=i.id)
    #         netinsert = ""
    #         for j in imdata:
    #             netduty = j.duty + j.markup
    #             netinsert = netduty
    #             AddImportsItem.objects.update(netduty=netduty)
                # subtotal = j.baseproductsalesprice + j.totalfrieght + j.netduty


                # AddImportsItem.objects.update(subtotal=subtotal)
                # if i.frieghtvalue:
                    # print(f"{i.frieghtvalue} = {i.freight} * ({i.frieghtvalue}/100")

    class Meta:
        verbose_name = 'Imports Item'
        verbose_name_plural = 'Imports Items'
        db_table = 'tbl_importsitems'
        managed = True


class ProductOption(models.Model):
    sku =  models.CharField(max_length=250, blank=True, null=True)
    optionname = models.CharField(max_length=250, blank=True, null=True)
    optionvalue = models.DecimalField(max_digits=5, decimal_places=2)
    markuprate = models.IntegerField(verbose_name ="Mark-Up Rate",default=35, blank=True, null=True)

    def __str__(self):
        return self.optionname


    class Meta:
        verbose_name = 'Products Options'
        verbose_name_plural = 'Products Options'
        db_table = 'tbl_productoption'
        managed = True

class AdditionalOption(models.Model):
    sku =  models.CharField(max_length=250, blank=True, null=True)
    optionname = models.CharField(max_length=250, blank=True, null=True)
    optionvalue = models.FloatField(blank=True, null=True)
    markuprate = models.IntegerField(verbose_name ="Mark-Up Rate",default=35, blank=True, null=True)

    def __str__(self):
        return self.optionname

    class Meta:
        verbose_name = 'Additional Options'
        verbose_name_plural = 'Additionals Options'
        db_table = 'tbl_additionaloption'
        managed = True