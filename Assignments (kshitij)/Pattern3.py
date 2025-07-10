n=int(input('Enter number of rows:'))

for i in range (0,n//2):
    print('* '*i)
for i in range ((n//2)-1,0,-1):
    print('* '*i)
print('\n')