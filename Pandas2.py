import pandas as pd

df=pd.DataFrame({'Sr no.':['5','6'],'Product ID':['105','106'],'Product name':['Pencil','Headphones'],'Price':['10','700'],'Quantity':['3','1']})
writer = pd.ExcelWriter('MyExcel2.xlsx', engine='xlsxwriter')

df.to_excel(writer)

writer.save()
print('Done.........')
