class Product1:
    pid=0
    pname=""
    price=0
    qty=0

    def accept(self):
        self.pid=int(input('Enter product Id:'))
        self.pname=input('Enter product name:')
        self.price = int(input('Enter price:'))
        self.qty = int(input('Enter quantity:'))

