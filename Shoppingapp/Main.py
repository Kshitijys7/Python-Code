from Shoppingapp.Customer import Customer
from Shoppingapp.Books import Books
from Shoppingapp.Electronics import Electronics
from Shoppingapp.Bill import Bill
from Shoppingapp.InvalidNameError import InvalidNameError
from Shoppingapp.InvalidCustID import InvalidCustID

lstcust=[]
lstprod=[]

while(True):
    print('1.Registration\n2.Login')
    ch=int(input('Enter your choice:'))

    if ch==1:
        print('----------------REGISTRATION-----------------')

        c1=Customer()
        c1.acceptCustomer()
        lstcust.append(c1)

        print('---------------Registered successfuly-----------')
        c1.showCustomer()

    elif ch==2:
        print('---------------LogIN-----------------')
        id=int(input('Enter your Customer ID:'))
        name=input('Enter your name:')

        for i in lstcust:
            try:
                if id==i.cid:
                    if name==i.cname:
                        print('------------Login successfully-----------')
                        print('To display shopping list.....press 1')
                        ch1=int(input())
                        if ch1==1:
                            while(True):
                                print('1.Books\n2.Electronics\n3.Display Cart with bill')
                                ch2=int(input('Enter your choice..'))
                                if ch2==1:
                                    b1=Books(int(input('Enter Product ID:')),int(input('Enter price:')),int(input('Enter quantity:')),input('Enter book name:'))
                                    b1.show()
                                    lstprod.append(b1)
                                    print('Product added to cart.....')

                                elif ch2==2:
                                    e1=Electronics(int(input('Enter Product ID:')),int(input('Enter price:')),int(input('Enter quantity:')),input('Enter name:'))
                                    e1.show()
                                    lstprod.append(e1)
                                    print('Product added to cart.....')

                                elif ch2==3:
                                    b=Bill(lstprod,0,0,0,0)
                                    b.calculateBill()
                                    b.show()

                                else:
                                    print('Invalid choice.....')

                                print('Do you want to continue shopping....??press 1')
                                choice = input()
                                if choice != '1':
                                    break

                    elif(name!=i.cname):
                        raise InvalidNameError(name,i.cname)

                elif(id!=i.cid):
                    raise InvalidCustID(id,i.cid)

            except InvalidCustID as c:
                print(c)
                break

            except InvalidNameError as s:
                print(s)
                break

    else:
        print('Invalid choice..........')

    print('Do you want to continue on main menu??press 1')
    choice=input()
    if choice!='1':
        break