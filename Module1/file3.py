from Module1.file2 import Address
from Module1.file1 import Product
class Customer:
    cid=0
    cname=""
    mob=0

    def acceptCustomer(self):
        self.cid=int(input('Enter customer ID:'))
        self.cname=input('Enter customer name:')
        self.mob=int(input('Enter customer mobile no.:'))
        Address.acceptAddress(self)
        Product.accept(self)

    def showCustomer(self):
        print('Customer ID\tCustomer name\tMobile no.')
        print(f'{self.cid}\t\t\t{self.cname}\t\t\t{self.mob}')
        Address.showAddress(self)
        Product.show(self)
