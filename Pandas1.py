import pandas as pd

data=pd.read_excel('MyExcel1.xlsx')
print(data)

result=data.sort_values('Price')
print(result)