class Product:
    pid=0
    price=0
    qty=0

    def accept(self):
        self.pid=int(input('Enter Product id:'))
        self.price=int(input('Enter price:'))
        self.qty=int(input('Enter quantity:'))

    def show(self):
        print('Product ID\tPrice\tQuantity')
        print(f'{self.pid}\t\t\t{self.price}\t\t{self.qty}')

class Books(Product):
    name=""
    def accept(self):
        super().accept()
        self.name=input('Enter name of the book:')

    def show(self):
        super().show()
        print('Book name:',self.name)

class Electronics(Product):
    name=""
    def accept(self):
        super().accept()
        self.name=input('Enter name of electronic product:')

    def show(self):
        super().show()
        print('Product name is:',self.name)