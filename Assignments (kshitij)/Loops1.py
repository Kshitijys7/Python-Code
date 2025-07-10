while(True):
        print('1.Area of circle\n2.Area of triangle\n3.Area of rectangle\n4.Factors\n5.Factorial\n6.Prime number\n7.Reverse')
        ch=int(input('Enter your choice:'))

        if(ch==1):
            r=int(input('Enter radius for circle:'))
            area=3.14*r*r
            print('Area of circle is:',area)

        elif(ch==2):
            b=int(input('Enter base of triangle:'))
            h=int(input('Enter height of triangle:'))
            area=0.5*b*h
            print('Area of triangle is:',area)

        elif(ch==3):
            l=int(input('Enter length of rectangle:'))
            b=int(input('Enter breadth of rectangle:'))
            area=l*b
            print('Area of rectangle is:',area)

        elif(ch==4):
            n=int(input('Enter the number whose factors you need to find:'))
            i=1
            while(i<=n):
                if(n%i==0):
                    print(i,end=" ")
                i=i+1

        elif(ch==5):
            n=int(input('Enter the number whose factorial you need to find:'))
            fac=1
            i=1
            while(i<=n):
                fac=fac*i
                i=i+1
            print('Factorial of ',{n},' is:',fac)

        elif(ch==6):
            n=int(input('Enter a number to check if it is prime:'))
            if(n>1):
                for i in range(2,n):
                    if(n%i==0):
                        print(n,' is a not prime number')
                    else:
                        print((n,'is a prime number'))

            print(n,'is a prime number')

        elif(ch==7):
            n=int(input('Enter the number you want to reverse:'))
            rev=0
            while(n>0):
                rem=n%10
                rev=rev*10+rem
                n=n//10
            print('Reverese of ',{n},'is:',rev)

        print('Do you want to continue? press 1')
        ch1=input()
        if(ch1!='1'):
            break
