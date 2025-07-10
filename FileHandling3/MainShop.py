import pickle

from FileHandling3.Shop import Product1

lstprod=[]
while(True):
    print('1.Accept data\n2.Save data in file\n3.Read data from file')
    ch=int(input('Enter your choice:'))

    if ch==1:
        n=int(input('Enter number of products you want:'))

        for i in range(n):
            p1=Product1()
            p1.accept()
            lstprod.append(p1)

    elif ch==2:
        with open('Binary_pickle2','bw') as pickle_file:
            pickle.dump(lstprod,pickle_file)

        print('Data saved..............')

    else:
        with open('Binary_pickle2','br') as pickle_file:
            lstprod1=pickle.load(pickle_file)

        print('Object from file.....')
        for i in lstprod1:
            print(f'Product ID:{i.pid}\nProduct name:{i.pname}\nPrice:{i.price}\nQuantity:{i.qty}')

    print('Do you want to continue?? press 1')
    choice=input()

    if choice!='1':
        break
