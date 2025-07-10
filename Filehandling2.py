import pickle

class Product1:
    def __init__(self,pid,pname,price,qty):
        self.pid=pid
        self.pname=pname
        self.price=price
        self.qty=qty

p1=Product1(int(input('Enter product id:')),input('Product name:'),int(input('Enter price:')),int(input('Enter quantity:')))

with open('Binary_pickle','bw') as pickle_file:
    pickle.dump(p1,pickle_file)

print('Done.....')

with open('Binary_pickle','br') as pickle_file:
    p2=pickle.load(pickle_file)

print('Object from file.....')
print(f'Product ID:{p2.pid}\nProduct name:{p2.pname}\nPrice:{p2.price}\nQuantity:{p2.qty}')

print('--------------------MULTIPLE OBJECTS IN A LIST----------------------')
lstprod=[]

n=int(input('Enter the number of products you want:'))

for i in range(n):
    p3=Product1(int(input('Enter product id:')),input('Product name:'),int(input('Enter price:')),int(input('Enter quantity:')))
    lstprod.append(p3)

with open('Binary_pickle2','bw') as pickle_file:
    pickle.dump(lstprod,pickle_file)

print('Done.........')

with open('Binary_pickle2','br') as pickle_file:
    lstprod1=pickle.load(pickle_file)

print('Object from file.....')

for i in lstprod1:
    print(f'Product ID:{i.pid}\nProduct name:{i.pname}\nPrice:{i.price}\nQuantity:{i.qty}')














'''
class Product:
    pid=0
    pname=" "
    def accept(self):
        self.pid=int(input('Enter product id:'))
        self.pname=input('Enter product name:')

    def display(self):
        print(self.pid)
        print(self.pname)

p1=Product()
p1.accept()

with open('Binary_pickle','bw') as pickle_file:
    pickle.dump(p1,pickle_file)

print('Done.....')

with open('Binary_pickle','br') as pickle_file:
    p2=pickle.load(pickle_file)

print('Object from file.....')

p2.display()
'''