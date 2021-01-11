from django.shortcuts import render
from .models import *
from django.views import View

class Home(View):
    def get(self, request):
        data = Product.objects.all().filter(id=2)
        items = AddDomesticItem.objects.all().filter(product_id=2)
        val = AddDomesticItem.objects.all().filter(product_id=2)
        options = ProductOption.objects.all()#.filter(sku__icontains=i.sku)
        cat = Category.objects.all()
        context = {'data':data,'items':items,'cat':cat,'val':val,'options':options}
        return render(request,'index.html',context)