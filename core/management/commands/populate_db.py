from django.core.management.base import BaseCommand
import pandas as pd
# from core.models import *
data = pd.read_excel(r"C:/Users/USER/Desktop/CostEngine/Costengine/FinalReport.xlsx",sheet_name='Sheet')

df = []
for sku,opt,val in zip(data["sku"],data["opt"],data["val"]):
    df.append(str(sku)+">>"+str(opt)+">>"+str(val))

print(df)



# for sku,option1,option2,option3,option4,option5,option6,val1,val2,val3,val4,val5,val6 in zip(data["SKU"],data["Option 1"],data["Option 2"],data["Option 3"],data["Option 4"],data["Option 5"],data["Option 6"],data["Value 1"],data["Value 2"],data["Value 3"],data["Value 4"],data["Value 5"],data["Value 6"]):
#     df.append(str(sku)+">>"+str(option1)+">>"+str(val1))
#     df.append(str(sku)+">>"+str(option2)+">>"+str(val2))
#     df.append(str(sku)+">>"+str(option3)+">>"+str(val3))
#     df.append(str(sku)+">>"+str(option4)+">>"+str(val4))
#     df.append(str(sku)+">>"+str(option5)+">>"+str(val5))
#     df.append(str(sku)+">>"+str(option6)+">>"+str(val6))

# print(len(df))
# count = 0
# for item in df:
#     try:
        
#         if item.split('>>')[2] != 'nan' and item.split('>>')[2] != 'nan' and item.split('>>')[2] != '-' and item.split('>>')[2] != '-':
#             sku=item.split('>>')[0]
#             optionname=item.split('>>')[1]
#             optionvalue=item.split('>>')[2].split('$')[1]
#             # print(sku,optionname,optionvalue)
#             count = count + 1
#     except:
#         continue
# print("Total Count : ",count)


from django.core.management.base import BaseCommand
from core.models import *

class Command(BaseCommand):
    args = '<Inserting ...>'
    help = 'Script populate data into ProductOption table'

    def _create_tags(self):
        for item in df:
            sku=item.split('>>')[0]
            optionname=item.split('>>')[1]
            optionvalue=item.split('>>')[2]
            # print(sku,optionname,optionvalue) 
            tlisp = ProductOption(sku=sku,optionname=optionname,optionvalue=optionvalue)
            tlisp.save()  
     
        # for item in df:
        #     try:        
        #         if item.split('>>')[2] != 'nan' and item.split('>>')[2] != 'nan' and item.split('>>')[2] != '-' and item.split('>>')[2] != '-':
        #             sku=item.split('>>')[0]
        #             optionname=item.split('>>')[1]
        #             optionvalue=item.split('>>')[2].split('$')[1]
        #             tlisp = ProductOption(sku=sku,optionname=optionname,optionvalue=optionvalue)
        #             tlisp.save()
                    # print(sku,optionname,optionvalue)
            # except Exception as e:
            #     print(e)
            #     continue
    def handle(self, *args, **options):
        self._create_tags()


'''
    For Run this file simple run the code

        python manage.py populate_db

'''