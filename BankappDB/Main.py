from BankappDB.Account import Account
from BankappDB.Savings import Savings
from BankappDB.Current import Current
from BankappDB.TMTLException import Transactionsmorethanlimit
from BankappDB.BLTLException import Balancelessthanlimit
from BankappDB.BankDB import BankDB

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
                print('1.Withdrawl\n2.Deposit\n3.Transfer money\n4.Display details\n5.Delete account')
                ch2=int(input('Enter your choice:'))

                if ch2==1:
                    amount=int(input('Enter amount to withdraw:'))
                    new_bal=BankDB.withdraw_money(accno,amount)
                    print('Withdrawl complete')
                    print('New balance=',new_bal)

                elif ch2==2:
                    amount = int(input('Enter amount to deposit:'))
                    new_bal = BankDB.deposit_money(accno, amount)
                    print('Deposit complete')
                    print('New balance=', new_bal)

                elif ch2==3:
                    accno_reciever=int(input('Enter account number of reciever'))
                    cname=BankDB.search(accno_reciever)
                    print('Account belongs to:',cname)
                    amount = int(input('Enter amount to transfer:'))
                    bal=BankDB.transfer_money(accno,accno_reciever,amount)

                    print('Transfered successfully.....')
                    print('Account balance=',bal)

                elif ch2==4:
                    lstcust=BankDB.display_data(accno)
                    for i in lstcust:
                        print(i)

                elif ch2==5:
                    confirm=input('Are you sure you want to delete account?? press y/n')
                    if confirm=='y':
                        status=BankDB.delete_record(accno)
                        if status:
                            print('Account deleted successfully.....')

                        else:
                            print('Account not deleted.....')

                    else:
                        print('Account not deleted.....')

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













