class Account:
    bankname=""
    def __init__(self,ano,bal):
        self.ano=ano
        self.bal=bal

    def display(self):
        print('Account no.',self.ano)
        print('Account balance',self.bal)
        print('Bank name',Account.bankname)

    @classmethod
    def bankdetails(cls):
        print('class method')
        Account.bankname="SBI"
        print('Bank name',cls.bankname)

    @staticmethod
    def checkdata():
        Account.bal=0
        return Account.bal

a1=Account(101,2000)
a1.display()
Account.bankdetails()
a1.display()