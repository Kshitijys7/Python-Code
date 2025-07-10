class Account:
    accno=1
    cname="Ramesh"
    bal=1000

    def accept(self):
        self.accno=int(input('Enter account number:'))
        self.cname=input('Enter customer name:')
        self.bal=int(input('Enter account balance:'))

    def show(self):
        print('Account number\tCustomer name\tAccount balance')
        print(f'{self.accno}\t\t\t\t{self.cname}\t\t\t\t{self.bal}')

    def getaccountNo(self):
        return self.accno

    def deposit(self,amount):
        self.bal=self.bal+amount

    def withdraw(self,amount):
        self.bal=self.bal-amount


lstacc=[]

while(True):
    print('1.Create Account\n2.Deposit\n3.Withdraw\n4.Show data\n5.Sorted data')
    ch=int(input('Enter your choice:'))

    if ch==1:
        n = int(input('Enter number of customers you want:'))
        for i in range(n):
            a1 = Account()
            a1.accept()
            lstacc.append(a1)

    elif ch==2:
        ano = int(input('Enter account number:'))
        for i in lstacc:
            if ano==i.getaccountNo():
                amount=int(input('Enter the amount you want to deposit:'))
                i.deposit(amount)
                print('New balance=',i.bal)

    elif ch==3:
        ano = int(input('Enter the account number:'))
        for i in lstacc:
            if ano == i.getaccountNo():
                amount=int(input('Enter the amount you want to withdraw:'))
                if amount<i.bal:
                    i.withdraw(amount)
                    print('New balance=', i.bal)

    elif ch==4:
        for i in lstacc:
            i.show()

    elif ch==5:
        temp=0
        for i in range(0,len(lstacc)):
            for j in range(i+1,len(lstacc)):
                if lstacc[i].accno>lstacc[j].accno:
                    temp=lstacc[i]
                    lstacc[i]=lstacc[j]
                    lstacc[j]=temp

        for i in lstacc:
            i.show()

    else:
        print('Invalid choice.....')

    print('Do you want to continue?? press 1')
    ch=input()
    if(ch!='1'):
        break