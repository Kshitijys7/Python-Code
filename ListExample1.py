list1=[]
n=int(input('Enter number of elements you want:'))

for j in range(1,n):
    list1.append(input('Enter a number:'))

def count_even_odd():
    count_even=0
    count_odd=0
    for i in range(1,n):
        if(i%2==0):
            count_even=count_even+1
        else:
            count_odd=count_odd+1

    print('Total even numbers in the list are:',count_even)
    print('Total odd numbers in the list are:', count_odd)

def min_max():
    min = list1[0]
    max = list1[0]
    for i in list1:
        if(i<min):
            min=i
    for i1 in list1:
        if(i1>max):
            max=i1

    print('Minimum number is:',min)
    print('Maximum number is:',max)

def avg():
    avg=0
    sum=0
    cnt=0
    for i in range(1,n):
        sum=sum+i
        cnt=cnt+1
    avg=sum/cnt
    print('Average is:',avg)

def count_prime():
    cnt=0
    for i in range(1,n):
        if(i<=1):
            continue
        for r in range (2,i):
            if(i%r==0):
                break
        else:
            cnt=cnt+1

    print('Total prime numbers are:',cnt)

def sort():
    temp=0
    for i in range(1,n):
        for j1 in range(i+1,n):
            if(i>j1):
                temp=i
                i=j1
                j1=temp
        print(i,end=" ")

def linear_search():
    key=int(input('Enter the element you need to find:'))
    flag=0
    for i in range(1,n):
        if(i==key):
            print('Element found.....')
            flag=1
            break
    if(flag==0):
        print('Element is not present in the list:')

def binary_search():
    first=0
    last=n
    mid=int((first+last)/2)
    key = int(input('Enter the element you need to find:'))
    flag = 0
    while(first<=last):
        if(key>int(list1[mid])):
            first=mid+1
        elif(key==int(list1[mid])):
            print('Element found.....')
            break
        elif(key<int(list1[mid])):
            last=mid-1
        mid=int((first+last)/2)

        if(first>last):
            print('Element not present in the list:')

while(True):
    print('1.Count even and odd numbers\n2.Find min and max number\n3.Average\n4.Count prime numbers\n5.Sort the elements\n6.Linear search\n7.Binary search')
    ch=int(input('Enter your choice:'))

    if(ch==1):
        count_even_odd()
    elif(ch==2):
        min_max()
    elif(ch==3):
        avg()
    elif(ch==4):
        count_prime()
    elif(ch==5):
        sort()
    elif(ch==6):
        linear_search()
    elif(ch==7):
        binary_search()

    print('Do you want to continue?press 1')
    ch1=input()
    if(ch1!='1'):
        break
