class Account:
    accno=1
    cname="Ramesh"
    bal=1000

    def accept(self):
        self.accno=int(input('Enter account number:'))
        self.cname=input('Enter customer name:')
        self.bal=int(input('Enter account balance:'))

    def show(self):
        print('Account number:',self.accno)
        print('Customer name:',self.cname)
        print('Account balance:',self.bal)

    def getaccountNo(self):
        return self.accno

    def deposit(self,amount):
        self.bal=self.bal+amount

    def withdraw(self,amount):
        self.bal=self.bal-amount


n=int(input('Enter number of customers you want:'))

lstacc=[]
for i in range(n):
    a1=Account()
    a1.accept()
    lstacc.append(a1)

while(True):
    print('1.Deposit\n2.Withdraw\n3.Show data')
    ch=int(input('Enter your choice:'))

    if ch==1:
        ano = int(input('Enter account number:'))
        for i in range(0,len(lstacc)):
            if ano==lstacc[i].accno:
                amount=int(input('Enter the amount you want to deposit:'))
                lstacc[i].deposit(amount)
                print('New balance=',lstacc[i].bal)

    elif ch==2:
        ano = int(input('Enter the account number:'))
        for i in range(0,len(lstacc)):
            if ano == lstacc[i].accno:
                amount=int(input('Enter the amount you want to withdraw:'))
                if amount<lstacc[i].bal:
                    lstacc[i].withdraw(amount)
                    print('New balance=', lstacc[i].bal)

    elif ch==3:
        for i in lstacc:
            i.show()

    else:
        print('Invalid choice.....')

    print('Do you want to continue?? press 1')
    ch=input()
    if(ch!='1'):
        break