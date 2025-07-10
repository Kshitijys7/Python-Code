class Product:
    def __init__(self,pid,pname,price):
        self.pid=pid
        self.pname=pname
        self.price=price

    def getProductId(self):
        return self.pid

    def getProductName(self):
        return self.pname

    def getProductPrice(self):
        return self.price

class Books(Product):
    def __init__(self,bid,bname,bprice,author,noofpages):
        super().__init__(bid,bname,bprice)
        self.author=author
        self.noofpages=noofpages

    def getAuthorName(self):
        return self.author

    def getNoofPages(self):
        return self.noofpages