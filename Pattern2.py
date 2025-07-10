n=int(input('Enter number of rows:'))
for i in range (0,n):
    for j in range (n-i,0,-1):
        print('* ',end=" ")
    print('\n')