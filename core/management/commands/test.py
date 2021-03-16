import sqlite3
from openpyxl import Workbook

row = 1
wb = Workbook()
wb['Sheet'].title = "Report of Automation"
sh1 = wb.active
sh1['A1'].value = 'sku'
sh1['B1'].value = 'Optionname'
sh1['C1'].value = 'Optionvalue'

conn = sqlite3.connect(r'C:/Users/USER/Desktop/CostEngine/Costengine/core/management/commands/db.sqlite3')
print("Opened database successfully!!")
cursor = conn.execute("SELECT sku,optionname,optionvalue from tbl_productoption")
count = 1
for row in cursor:
   sh1['A'+str(count)].value = row[0]
   sh1['B'+str(count)].value = row[1]
   sh1['C'+str(count)].value = row[2]
   
   count = count + 1
   
print("Operation done successfully!!")
conn.close()

wb.save("FinalReport.xlsx")