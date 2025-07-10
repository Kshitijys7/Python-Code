from Bankapp.Account import Account
from Bankapp.Processing import Processing

class Current(Account,Processing):
    def __init__(self,ano,cname,bal,nameoforg,maxNOT,type):
        super().__init__(ano,cname,bal,type)
        self.nameoforg=nameoforg
        self.maxNOT=maxNOT


    def deposit(self, amount):
        self.bal = self.bal + amount

    def withdraw(self, amount):
        self.bal = self.bal -amount

    def __str__(self):
        return f'{self.ano}\t{self.cname}\t{self.bal}\t{self.nameoforg}'

