class Shopping:
    pid=1
    pname="abc"
    price=100
    qty=1
    total=0

    def accept(self):
        self.pid=int(input('Enter product id:'))
        self.pname=input('Enter Product name:')
        self.price=int(input('Enter price:'))
        self.qty=int(input('Enter the quantity:'))

    def calculate(self):
        self.total=self.price*self.qty

    def show(self):
        print(f"{self.pid}\t\t\t{self.pname}\t\t\t{self.price}\t\t{self.qty}\t\t{self.total}")

n=int(input('Enter number of products you want:'))
lstprod=[]


for i in range(0,n):
    s1=Shopping()
    s1.accept()
    s1.calculate()

    if i==0:
        lstprod.append(s1)

    else:
        if s1.total>lstprod[0].total:
            temp=lstprod[0]
            lstprod[0]=s1
            lstprod.append(temp)
        else:
            lstprod.append(s1)



print('Product ID\tProduct name\tPrice\tQuantity\tTotal')
for i in lstprod:
    i.show()

Total_price=0
GST=0
Final_total=0
for i in lstprod:
    Total_price=Total_price+i.total
GST=0.05*Total_price
Final_total=Total_price+GST

print('Total price-------',Total_price)
print('GST---------------',GST)
print('Final total-------',Final_total)