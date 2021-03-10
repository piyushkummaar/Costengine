from django.core.management.base import BaseCommand
import pandas as pd
# from core.models import *
data = pd.read_excel(r"pathoffileupdalod")#C:/Users/USER/Desktop/CostEngine/product_finaloption.xlsx",sheet_name='Domestic_productFinalOption_wit')

df = []
for sku,option1,option2,option3,option4,val1,val2,val3,val4 in zip(data["SKU"],data["OPTION - 1"],data["OPTION - 2"] ,data["OPTION - 3"],data["OPTION - 4"],data["VALUE - 1"],data["VALUE - 2"],data["VALUE - 3"],data["VALUE - 4"]):
    df.append(str(sku)+">>"+str(option1)+">>"+str(val1))
    df.append(str(sku)+">>"+str(option2)+">>"+str(val2))
    df.append(str(sku)+">>"+str(option3)+">>"+str(val3))
    df.append(str(sku)+">>"+str(option4)+">>"+str(val4))

print(len(df))
        

from django.core.management.base import BaseCommand
from core.models import *

class Command(BaseCommand):
    args = '<Inserting ...>'
    help = 'Script populate data into ProductOption table'

    def _create_tags(self):        
        for data in df:
            try:
                if data.split('>>')[2] != 'nan' and data.split('>>')[2] != 'nan' and data.split('>>')[2] != '-' and data.split('>>')[2] != '-':
                    tlisp = ProductOption(sku=data.split('>>')[0],optionname=data.split('>>')[1],optionvalue=data.split('>>')[2].split('$')[1])
                    tlisp.save()
            except Exception as e:
                print(e)
        
    def handle(self, *args, **options):
        self._create_tags()


'''
    For Run this file simple run the code

        python manage.py populate_db

'''