n=int(input('Enter number of rows:'))
num=65

for i in range (0,n):
    for j in range (0,i+1):
        print(chr(num),end=" ")
        num=num+1
    print("\n")