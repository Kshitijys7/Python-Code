print('1.Area of Triangle')
print('2.Area of Circle')
print('3.Area of Rectangle')

ch=int(input('Enter your choice:'))
if(ch==1):
    b=int(input('Enter the base of triangle:'))
    h=int(input('Enter the height of triangle:'))
    area=0.5*b*h
    print('Area of triangle is:',area)

elif(ch==2):
    r=int(input('Enter the radius for circle:'))
    area=3.14*r*r
    print('Area of circle is:',area)

elif(ch==3):
    l=int(input('Enter length of rectangle:'))
    b=int(input('Enter breadth of rectangle'))
    area=l*b
    print('Area of rectangle is:',area)
