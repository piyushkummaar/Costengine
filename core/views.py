from django.shortcuts import render,redirect
from .models import *
from django.http import JsonResponse
from django.core import serializers
# Create your views here.
def home(request):
    sku = 'LTCD2S'
    if request.method == 'POST':
        region =  request.POST.get('value', '')
        cat = Category.objects.filter(region_id=region)
        data = {}
        count = 1
        for i in cat:
            data["val"+str(count)] = i.category
            count += 1
        return JsonResponse({"data": data}, status=200)

    reg = Region.objects.all()
    template_name = 'index.html'
    context = {'reg':reg}
    return render(request,template_name,context)

def subcat(request):
    if request.is_ajax and request.method == 'POST':
        subca =  request.POST.get('value', '')
        region = request.POST.get('region', '')
        if region == 'Domestic': 
            subcat = SubCategory.objects.filter(region_id=1)
        else:
            subcat = SubCategory.objects.filter(region_id=2)
        data = {}
        count = 1
        for i in subcat:
            data["val"+str(count)] = i.subcategory
            count += 1
        return JsonResponse({"data": data}, status=200)

def productname(request):
    if request.is_ajax and request.method == 'POST':
        region = request.POST.get('region', '')
        if region == 'Domestic': 
            prodata = DomesticProduct.objects.filter(region_id=1)
        elif region == 'Imports':
            prodata = ImportsProduct.objects.filter(region_id=2)
        data = {}
        count = 1
        for i in prodata:
            data["val"+str(count)] = i.productname +">>"+i.sku 
            count += 1
        return JsonResponse({"data": data}, status=200) 

def productget(request):
    if request.is_ajax and request.method == 'POST':
        region = request.POST.get('region', '')
        sku = request.POST.get('sku','')
        if region == 'Domestic': 
            prodata = DomesticProduct.objects.filter(sku=sku)
            for i in prodata:
                items = AddDomesticItem.objects.all().filter(product_id=i.id)
                val = AddDomesticItem.objects.all().filter(product_id=i.id)
            options = ProductOption.objects.all().filter(sku__icontains=sku)    
            return render(request, 'index.html',{'prodata':prodata,'options':options,'items':items,'val':val})
        elif region == 'Imports':
            improdata = ImportsProduct.objects.filter(sku=sku)
            for i in improdata:
                items = AddImportsItem.objects.all().filter(product_id=i.id)
                val = AddImportsItem.objects.all().filter(product_id=i.id)
            options = ProductOption.objects.all().filter(sku__icontains=sku)
            addoptions = AdditionalOption.objects.all().filter(sku__icontains=sku)
            return render(request, 'index.html',{'improdata':improdata,'options':options,'addoptions':addoptions,'items':items,'val':val})

def table(request):
    sku = 'LTCD2S'  
    if sku == 'LTCD2S':
        prodata = DomesticProduct.objects.filter(sku=sku)
        for i in prodata:
            items = AddDomesticItem.objects.all().filter(product_id=i.id)
            val = AddDomesticItem.objects.all().filter(product_id=i.id)
        options = ProductOption.objects.all().filter(sku__icontains=sku)    
        return render(request, 'index.html',{'prodata':prodata,'options':options,'items':items,'val':val})
    elif sku == 'LCDHT':
        improdata = ImportsProduct.objects.filter(sku=sku)
        for i in improdata:
            items = AddImportsItem.objects.all().filter(product_id=i.id)
            val = AddImportsItem.objects.all().filter(product_id=i.id)
        options = ProductOption.objects.all().filter(sku__icontains=sku)
        addoptions = AdditionalOption.objects.all().filter(sku__icontains=sku)
        return render(request, 'index.html',{'improdata':improdata,'options':options,'addoptions':addoptions,'items':items,'val':val})
