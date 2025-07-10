class InvalidCustID(Exception):
    def __init__(self,id,custid,msg="Invalid customer ID"):
        self.id=id
        self.custid=custid
        self.msg=msg

    def __str__(self):
        return f'{self.id}->{self.msg}'