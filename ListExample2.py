n=int(input('Enter the number of elements you want in the list:'))
list1=[]
for r in range (0,n):
    list1.append(input('Enter a value:'))

k=int(input('Enter the number of times you want to rotate the list:'))

temp=0
for j in range (1,k+1):
    for p in range (1,n):
        temp=list1[p]
        list1[p]=list1[0]
        list1[0]=temp

    for i in list1:
        print(i,end=" ")

    print()