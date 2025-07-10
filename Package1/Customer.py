class Customer:
    def __init__(self,cid,cname,prodlst,):
        self.cid=cid
        self.cname=cname
        self.prodlst=prodlst

    def getCustomerId(self):
        return self.cid

    def getCustName(self):
        return self.cname

    def getProductList(self):
        return self.prodlst

