from Bankapp.Account import Account
from Bankapp.Savings import Savings
from Bankapp.Current import Current
from Bankapp.TMTLException import Transactionsmorethanlimit
from Bankapp.BLTLException import Balancelessthanlimit
from Bankapp.BankDB import BankDB

lstcust=[]

while(True):
    print('1.Registration\n2.Login')
    ch=int(input('Enter your choice:'))

    if ch==1:

        print('----------------REGISTRATION-----------------')
        flag=0

        while(True):
            print('1.Savings\n2.Current')
            ch1=int(input('Enter your choice:'))
            if ch1==1:
                try:
                    s1=Savings(int(input('Enter account no:')),input('Enter customer name'),int(input('Enter balance:')),input('Enter name of organization:'),int(input('Enter max no of trasactions:')),'Savings')
                    lstcust.append(s1)
                    flag=1
                    if s1.maxNOT>6:
                        raise Transactionsmorethanlimit(s1.maxNOT)

                except Transactionsmorethanlimit as t1:
                    print(t1)
                    break

                if(flag==1):
                    print('---------------Registered successfuly-----------')
                    break

                else:
                    print('Not Registered---------------')
                    break

            elif ch1==2:
                try:
                    c1=Current(int(input('Enter account no')),input('Enter customer name'),int(input('Enter balance:')),input('Enter name of organization:'),int(input('Enter max no of trasactions:')),'Current')
                    lstcust.append(c1)
                    flag=1

                    if(c1.bal<1000):
                        raise Balancelessthanlimit(c1.bal)

                except Balancelessthanlimit as b1:
                    print(b1)
                    break

                if(flag==1):
                    print('---------------Registered successfuly-----------')
                    break

                else:
                    print('Not Registered---------------')
                    break

            else:
                print('Invalid choice:')


    elif ch==2:
        print('-----------LogIN Portal-------------' )
        accno=int(input('Enter account number:'))
        custname=input('Enter customer name:')

        if BankDB.verification(accno,custname):
            print('-----------Login Successfully-------------')

            while(True):
                print('1.Withdrawl\n2.Deposit\n3.Display details')
                ch2=int(input('Enter your choice:'))

                if ch2==1:
                    amount=int(input('Enter amount to withdraw:'))
                    s1.withdraw(amount)
                    print('New Balance:',s1.bal)
                elif ch2==2:
                    s.deposit(int(input('Enter amount to deposit:')))
                    print('New Balance:', s.bal)

                elif ch2==3:
                    print('Hi')

                else:
                    print('Invalid choice:')

                print('Do you want to continue with transactions??press 1')
                choice1=input()
                if(choice1!='1'):
                    break
        else:
            print('Login failed.....')

    else:
        print('Invalid choice..')

    print('Do you want to continue on main menu??press 1')
    choice = input()
    if (choice != '1'):
        break













