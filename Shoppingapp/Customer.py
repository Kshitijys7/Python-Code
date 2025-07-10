from Shoppingapp.Address import Address
class Customer:
    cid = 0
    cname = ""
    mob = 0

    def acceptCustomer(self):
        self.cid = int(input('Enter customer ID:'))
        self.cname = input('Enter customer name:')
        self.mob = int(input('Enter customer mobile no.:'))
        Address.acceptAddress(self)

    def showCustomer(self):
        print('Customer ID:',self.cid)
        print('Customer name:',self.cname)
        print('Mobile no.',self.mob)
        Address.showAddress(self)

