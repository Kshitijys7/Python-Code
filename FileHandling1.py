f1=open('data.txt','w')
f1.write('Hello\nHi\nBye-bye')
f1=open('data.txt','r')
print(f1.readline())

f1=open('data.txt','r')
f2=open('data1.txt','w')

for i in f1:
    f2.write(i)

print('Done copying.....')
f2=open('data1.txt','r')
#print(f2.readline())
#print(f2.readline(),end=" ")
#print(f2.readline(3))
print(f2.read())

f1.close()
f2.close()
