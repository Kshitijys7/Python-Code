from Module1.file3 import Customer
lstCustomer=[]
n=int(input('Enter number of customers:'))

for i in range(n):
    c1=Customer()
    c1.acceptCustomer()
    lstCustomer.append(c1)

for i in lstCustomer:
    i.showCustomer()