n=int(input('Enter number of rows:'))
num=1

for i in range (n,0,-1):
    for j in range (i,0,-1):
        print(num,end=" ")
        num=num+1
    num=1
    print('\n')
