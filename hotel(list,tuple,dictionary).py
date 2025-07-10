def displaymenu(list1):
	for i in range(0,len(list1)):
		print(f"{(i + 1)}  {list1[i]}")

def Order(order):
	print('Order is..')
	for i in range(0,len(order[1])):
		print(f"{i+1}  {order[0][i]}  {order[1][i]}")


veg=[{"Food":"Paneer","Price":"100"},
	 {"Food":"DalFry","Price":"150"},
	 {"Food":"MixVeg","Price":"200"},
	 {"Food":"Rajma","Price":"300"}
	 ]

nonveg=[{"Food":"Chicken Masala","Price":"100"},
	 {"Food":"Chicken Handi","Price":"150"},
	 {"Food":"Mutton Handi","Price":"200"},
	 {"Food":"Chicken Biryani","Price":"300"}
	 ]

starter=[{"Food":"Vegcrispy","Price":"100"},
	 {"Food":"AluCutlet","Price":"150"},
	 {"Food":"Tandoori","Price":"200"},
	 {"Food":"Panipuri","Price":"300"}
	 ]

menucard=(starter,veg,nonveg)

lstitem=[]
lstprice=[]
order=(lstitem,lstprice)
total=0


def show_bill(order):
	print('---------Bill---------')
	print('Srno\tItem name\tItem Price')
	for i in range(0, len(order[1])):
		print(f"{i + 1}\t\t{order[0][i]}\t\t{order[1][i]}")

	print('Total : ',total)
	print('CGST ',cgst)
	print('SGST ',sgst)
	print('Final Bill ',finaltotal)

print('-------------MENU---------------')
while(True):
	print('1-Starter')
	print('2-Veg')
	print('3-Non-Veg')
	#print('4-Bill')

	ch=int(input('enter your choice..'))
	if ch==1:
		displaymenu(menucard[0])
		ch1 = int(input('Enter your choice..'))
		if ch1 <= len(menucard[0]):
			order[0].append(menucard[0][ch1-1]["Food"])
			order[1].append(menucard[0][ch1-1]["Price"])
		Order(order)

	elif ch==2:
		displaymenu(menucard[1])
		ch1 = int(input('Enter your choice..'))
		if ch1 <= len(menucard[1]):
			order[0].append(menucard[1][ch1-1]["Food"])
			order[1].append(menucard[1][ch1-1]["Price"])
		Order(order)

	elif ch==3:
		displaymenu(menucard[2])
		ch1 = int(input('Enter your choice..'))
		if ch1 <= len(menucard[2]):
			order[0].append(menucard[2][ch1-1]["Food"])
			order[1].append(menucard[2][ch1-1]["Price"])
		Order(order)

	else:
		print('Invalid choice......')

	choice=int(input('To continue on main menu press 1.....To print the bill press any other key.....'))
	if choice!=1:
		for i in range(0, len(order[1])):
			total = total + int(order[1][i])

		cgst = total * 0.05;
		sgst = total * 0.05;
		finaltotal = total + cgst + sgst

		show_bill(order)
		break;


print('-------Thank You, Visit again............')