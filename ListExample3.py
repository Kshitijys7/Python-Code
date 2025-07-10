Starter=['Vegcrispy','AluCutlet','Tandoori']
Starter_price=[100,200,300]
Vegmenu=['Paneer','Bharta','MixVeg']
Veg_price=[150,170,120]
Nonvegmenu=['Chicken Masala','Chicken Handi','Mutton Handi']
Nonveg_price=[200,500,550]
total = []
Qauntity = []
Total_bill=0
item_name=[]

print('------------------Menu------------------')

print('Starters:\t\t\tPrice:')
for i in range (0,len(Starter)):
    #print(f'{Starter[i]}      {Starter_price[i]}')
    print(Starter[i],'\t\t\t',Starter_price[i])

print('------------------VEG------------------')

print('Veg:\t\t\t\tPrice:')
for i in range (0,len(Vegmenu)):
    print(Vegmenu[i],'\t\t\t\t',Veg_price[i])

print('----------------NONVEG------------------')

print('NonVeg:\t\t\t\tPrice:')
for i in range (0,len(Nonvegmenu)):
    print(Nonvegmenu[i],'\t\t',Nonveg_price[i])


def price(cost,qty,name):
    total_price=cost*qty
    Qauntity.append(qty)
    total.append(total_price)
    item_name.append(name)

while(True):
    print('1.Starter\n2.Veg\n3.Nonveg')
    ch = int(input('Enter your choice:'))

    if(ch==1):
        while (True):
            print('1.Vegcrispy\n2.AluCutlet\n3.Tandoori')
            ch1=int(input('Enter your choice:'))

            if(ch1==1):
                qty=int(input('Enter the quantity you want:'))
                price(Starter_price[0],qty,Starter[0])

            elif(ch1==2):
                qty = int(input('Enter the quantity you want:'))
                price(Starter_price[1], qty,Starter[1])

            elif (ch1 == 3):
                qty = int(input('Enter the quantity you want:'))
                price(Starter_price[2], qty,Starter[2])

            else:
                print('Invalid choice:')

            print('Do you want to continue??press 1\nTo return to main menu press 0')
            choice=input()
            if(choice!='1'):
                break

    elif(ch==2):
        while (True):
            print('1.Paneer\n2.Bharta\n3.MixVeg')
            ch1=int(input('Enter your choice:'))

            if (ch1 == 1):
                qty = int(input('Enter the quantity you want:'))
                price(Veg_price[0], qty,Vegmenu[0])

            elif (ch1 == 2):
                qty = int(input('Enter the quantity you want:'))
                price(Veg_price[1], qty,Vegmenu[1])

            elif (ch1 == 3):
                qty = int(input('Enter the quantity you want:'))
                price(Veg_price[2], qty,Vegmenu[2])

            else:
                print('Invalid choice:')

            print('Do you want to continue??press1\nTo return to main menu press 0')
            choice = input()
            if (choice!= '1'):
                break

    elif(ch==3):
        while (True):
            print('1.Chicken Masala\n2.Chicken Handi\n3.Mutton Handi')
            ch1=int(input('Enter your choice:'))

            if (ch1 == 1):
                qty = int(input('Enter the quantity you want:'))
                price(Nonveg_price[0], qty,Nonvegmenu[0])

            elif (ch1 == 2):
                qty = int(input('Enter the quantity you want:'))
                price(Nonveg_price[1], qty,Nonvegmenu[1])

            elif (ch1 == 3):
                qty = int(input('Enter the quantity you want:'))
                price(Nonveg_price[2], qty,Nonvegmenu[2])

            else:
                print('Invalid choice:')

            print('Do you want to continue??press1\nTo return to main menu press 0')
            choice = input()
            if (choice!= '1'):
                break

    else:
        print('Invalid choice:')

    print('Do you want to continue on main menu??press1')
    choice = input()
    if (choice!= '1'):
       break

for i in range(0,len(total)):
    Total_bill=Total_bill+int(total[i])


def show_bill():
    print('Sr no\tItem name\tQuantity\tTotal')
    for i in range(0,len(total)):
        print(i+1,'\t\t',item_name[i],'\t\t',Qauntity[i],'\t\t',total[i])

show_bill()

sgst=Total_bill*0.05
cgst=Total_bill*0.08
final_bill=Total_bill+sgst+cgst

print('Total Bill-------------',Total_bill)
print('sgst-------------------',sgst)
print('cgst-------------------',cgst)
print('Final Bill-------------',final_bill)