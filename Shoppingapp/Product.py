class Product:
    def __init__(self,pid,price,qty):
        self.pid=pid
        self.price=price
        self.qty=qty

    def __str__(self):
        return f'Product ID:{self.pid}\nPrice:{self.price}\nQuantity:{self.qty}'

