import pandas as pd
#import cx_Oracle
from openpyxl import load_workbook

book = load_workbook('MyExcel3.xlsx')

writer = pd.ExcelWriter('MyExcel3.xlsx', engine='openpyxl')

writer.book = book

writer.sheets = dict((ws.title, ws) for ws in book.worksheets)

df=pd.DataFrame({'Sr no.':['5','6'],'Product ID':['105','106'],'Product name':['Pencil','Headphones'],'Price':['10','700'],'Quantity':['3','1']})

df1=pd.DataFrame({'Sr no.':['7','8'],'Product ID':['107','108'],'Product name':['Cap','Ball'],'Price':['50','70'],'Quantity':['3','4']})


df.to_excel(writer)
df1.to_excel(writer)

writer.save()
print('Done..........')