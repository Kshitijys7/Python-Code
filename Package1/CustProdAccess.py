from Package1.Customer import Customer
#from Package1.Product import Product
from Package1.Product import Books

booklist=[]
n=int(input('Enter no. of books customer wants:'))

for i in range(n):
    b1=Books(int(input('Book ID:')),input('Book name:'),int(input('Book price:')),input('Author:'),int(input('Number of Pages:')) )
    booklist.append(b1)



c1=Customer(int(input('Customer ID:')),input('Customer name:'),booklist)

print('Customer ID:',c1.getCustomerId())
print('Customer name:',c1.getCustName())

for i in booklist:
    print('Book ID:',i.getProductId())
    print('Book name:',i.getProductName())
    print('Book Price:',i.getProductPrice())
    print('Author name:',i.getAuthorName())
    print('No. of pages:',i.getNoofPages())
