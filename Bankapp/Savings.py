from Bankapp.Account import Account
from Bankapp.Processing import Processing
from Bankapp.BankDB import BankDB

class Savings(Account,Processing):
    def __init__(self,ano,cname,bal,nameoforg,maxNOT,type):
        super().__init__(ano,cname,bal,type)
        self.maxNOT=maxNOT
        self.nameoforg=nameoforg
        BankDB.insertValues(ano,cname,bal,nameoforg,maxNOT,type)

    def __str__(self):
        return f'{self.ano}\t{self.cname}\t{self.bal}\t{self.maxNOT}'

    def checkBalance(func):
        def inner(self,amount):
            if self.bal<1000:
                print('Sorry cannot withdraw.....Balance is less than 1000')
            else:
                self.bal=self.bal-amount
            return self.bal
        return inner

    @checkBalance
    def withdraw(self,amount):
        self.bal=self.bal-amount

    def deposit(self, amount):
        self.bal=self.bal+amount
