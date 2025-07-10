from Shoppingapp.Product import Product
from Shoppingapp.ProdDescription import ProdDescription
class Electronics(Product,ProdDescription):

    def __init__(self,pid,price,qty,name):
        super().__init__(pid,price,qty)
        self.name=name

    def show(self):
        self.description()
        super().__str__()
        print('Product name is:',self.name)

    def description(self):
        print('------------Thankyou for your time, we hope to see you again-------------')