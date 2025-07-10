class Account:
    def __init__(self,ano,bal):
        self.ano=ano
        self.__bal=bal

    @property
    def bal(self):
        if self.__bal<1000:
            print('Balance is less.....')
        else:
            return self.__bal

    @bal.setter
    def bal(self,bal):
        if bal>50000:
            print('Cannot deposit more than 50000')
        else:
            self.__bal=bal


    def withdraw(self,bal):
        self.__bal=self.__bal-bal


a1=Account(101,2000)
a1.bal=3000
print(a1.bal)
a1.withdraw(2200)
print(a1.bal)
a1.bal=51000
print('hi')
print(a1.bal)

