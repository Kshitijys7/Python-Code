class Product:
    pid=0
    pname=""
    price=0
    qty=0

    def accept(self):
        self.pid=int(input('Enter Product id:'))
        self.pname=input('Enter product name:')
        self.price=int(input('Enter price:'))
        self.qty=int(input('Enter quantity:'))
        Address.acceptAddress(self)

    def show(self):
        print('Product ID\tProduct name\tPrice\tQuantity')
        print(f'{self.pid}\t\t\t{self.pname}\t\t\t{self.price}\t\t\t{self.qty}')
        Address.showAddress(self)

class Address:
    city=""
    state=""
    pin=0

    def acceptAddress(self):
        self.city=input('Enter name of the city:')
        self.state=input('Enter name of the state:')
        self.pin=int(input('Enter PIN number:'))
        Customer.acceptCustomer(self)

    def showAddress(self):
        print('City\tState\t\tPin')
        print(f'{self.city}\t{self.state}\t{self.pin}')
        Customer.showCustomer(self)

class Customer:
    cid=0
    cname=""
    mob=0

    def acceptCustomer(self):
        self.cid=int(input('Enter customer ID:'))
        self.cname=input('Enter customer name:')
        self.mob=int(input('Enter customer mobile n.:'))

    def showCustomer(self):
        print('Customer ID\tCustomer name\tMobile no.')
        print(f'{self.cid}\t\t\t{self.cname}\t\t\t{self.mob}')

n=int(input('Enter no. of products:'))
lstproduct=[]

for i in range(n):
    p1=Product()
    p1.accept()
    lstproduct.append(p1)

for i in lstproduct:
    i.show()
