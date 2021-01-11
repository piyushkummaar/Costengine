from django.shortcuts import render
from .models import *
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def index(request):
    pro = Product.objects.all()
    region = Region.objects.all()
    cat = Category.objects.all()
    subcat = SubCategory.objects.all().filter(category_resign=1)
    subsubcat = SubSubCategory.objects.all()
    template_name = 'index.html'
    # for i in pro:
    #     print(i.sku)
    #     print(i.quantities.all())
    #     print(i.price.all())
    context = {'pro':pro,'r':region,'subcat':subcat,'subsubcat':subsubcat,'cat':cat}
    return render(request, template_name, context)


