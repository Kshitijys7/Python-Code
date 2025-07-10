def displaymenu(lstv,lstp):
	for i in range(0,len(lstv)):
		print(f"{(i + 1)}  {lstv[i]}  {lstp[i]}")

def Order(tuple1):
	print('Order is..')
	for i in range(0,len(tuple1[1])):
		print(f"{i+1}  {tuple1[0][i]}  {tuple1[1][i]}")


lstvegmenu=['Paneer','Bharta','Mixveg','Rajma']
lstvegprice=[100,150,200,300]
tuplev=(lstvegmenu,lstvegprice)

Startermenu=['Vegcrispy','AluCutlet','Tandoori','Panipuri']
Starter_price=[100,200,300,100]
tuples=(Startermenu,Starter_price)

lstnonvegmenu=['Chicken masala','Chicken Handi','Mutton Handi','Chicken Biryani']
lstnonvegprice=[100,150,200,300]
tuplen=(lstnonvegmenu,lstnonvegprice)

lstitem=[]
lstprice=[]
tuple1=(lstitem,lstprice)
total=0


def show_bill(tuple1):
	print('---------Bill---------')
	print('Srno\tItem name\tItem Price')
	for i in range(0, len(tuple1[1])):
		print(f"{i + 1}\t\t{tuple1[0][i]}\t\t{tuple1[1][i]}")

	print('Total : ',total)
	print('CGST ',cgst)
	print('SGST ',sgst)
	print('Final Bill ',finaltotal)
	print('-------Thank You, Visit again............')
print('-------------MENU---------------')
while(True):
	print('1-Starter')
	print('2-Veg')
	print('3-Non-Veg')
	print('4-Bill')

	ch=int(input('enter your choice..'))
	if ch==1:
		displaymenu(tuples[0], tuples[1])
		ch1 = int(input('Enter your choice..'))
		if ch1 <= len(tuples[0]):
			tuple1[0].append(Startermenu[ch1 - 1])
			tuple1[1].append(Starter_price[ch1 - 1])
		Order(tuple1)

	elif ch==2:
		displaymenu(tuplev[0],tuplev[1])
		ch1 = int(input('Enter your choice..'))
		if ch1 <= len(tuplev[0]):
			tuple1[0].append(lstvegmenu[ch1-1])
			tuple1[1].append(lstvegprice[ch1-1])
		Order(tuple1)

	elif ch==3:
		displaymenu(tuplen[0],tuplen[1])
		ch1 = int(input('Enter your choice..'))
		if ch1 <= len(lstvegmenu):
			tuple1[0].append(lstnonvegmenu[ch1 - 1])
			tuple1[1].append(lstnonvegprice[ch1 - 1])
		Order(tuple1)

	elif ch==4:
		for i in range(0, len(tuple1[1])):
			total = total + tuple1[1][i]

		cgst = total * 0.05;
		sgst = total * 0.05;
		finaltotal = total + cgst + sgst

		show_bill(tuple1)

	else:
		print('Invalid choice......')

	choice=int(input('do you want to continue?? press 1'))
	if choice!=1:
		break;


