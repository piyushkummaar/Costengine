from django.shortcuts import render,redirect
from .models import *
from django.http import JsonResponse,HttpResponse
from django.core import serializers

def home(request):
    reg = Region.objects.all()
    template_name = 'index.html'
    if request.method == 'POST':
        region = request.POST.get('region','')
        sku = request.POST.get('sku','')
        test,th = None, None
        if region == 'Domestic':
            prodata = DomesticProduct.objects.filter(sku=sku)
            for i in prodata:
                items = AddDomesticItem.objects.all().filter(product_id=i.id)
                test = len(items) - 1
                th = AddDomesticItem.objects.all().filter(product_id=i.id)[:test]
                val = AddDomesticItem.objects.all().filter(product_id=i.id)
            options = ProductOption.objects.all().filter(sku__icontains=sku)    
            return render(request, template_name,{'reg':reg,'test':th,'prodata':prodata,'options':options,'items':items,'val':val})
        elif region == 'Imports':
            improdata = ImportsProduct.objects.filter(sku=sku)
            for i in improdata:
                items = AddImportsItem.objects.all().filter(product_id=i.id)
                test = len(items) - 1
                th = AddDomesticItem.objects.all().filter(product_id=i.id)[:test]
                val = AddImportsItem.objects.all().filter(product_id=i.id)
            options = ProductOption.objects.all().filter(sku__icontains=sku)
            addoptions = AdditionalOption.objects.all().filter(sku__icontains=sku)
            return render(request, template_name,{'reg':reg,'improdata':improdata,'test':th,'options':options,'addoptions':addoptions,'items':items,'val':val})
    
    context = {'reg':reg}
    return render(request,template_name,context)

def main(request):
    if request.is_ajax and request.method == 'POST':
        region =  request.POST.get('value', '')
        cat = Category.objects.filter(region_id=region)
        data = {}
        count = 1
        for i in cat:
            data["val"+str(count)] = i.category +">>"+str(i.id)
            count += 1
        return JsonResponse({"data": data}, status=200)


def subcat(request):
    if request.is_ajax and request.method == 'POST':
        subca =  request.POST.get('value', '')
        region = request.POST.get('region', '')
        if region == 'Domestic':
            subcat = SubCategory.objects.filter(region_id=1,category_id=subca)
        elif region == 'Imports':
            subcat = SubCategory.objects.filter(region_id=2,category_id=subca)
        data = {}
        count = 1
        for i in subcat:
            data["val"+str(count)] = i.subcategory +">>"+str(i.id)+">>"+str(i.category.id)
            count += 1
        return JsonResponse({"data": data}, status=200)

def productname(request):
    if request.is_ajax and request.method == 'POST':
        seprate =  request.POST.get('value', '')
        region = request.POST.get('region', '')
        subid = seprate.split('>')[0]
        catid = seprate.split('>')[1]
        if region == 'Domestic': 
            prodata = DomesticProduct.objects.filter(region_id=1,category_id=catid,subcatagory_id=subid)
        elif region == 'Imports':
            prodata = ImportsProduct.objects.filter(category_id=catid,subcatagory_id=subid)
        data = {}
        count = 1
        for i in prodata:
            data["val"+str(count)] = i.productname +">>"+i.sku 
            count += 1
        return JsonResponse({"data": data}, status=200) 