while(True):
        print('1.Area of circle\n2.Area of triangle\n3.Area of rectangle\n4.Factors\n5.Factorial\n6.Prime number\n7.Reverse\n8.Sum of digits\n9.Fibonacci series\n10.Perfect number\n11.Power\n12.Armstrong number\n13.Palindrome number\n')
        ch=int(input('Enter your choice:'))

        if(ch==1):
            def calculate(r):
                area=3.14*r*r
                print('Area of circle is:',area)

            print(calculate(int(input('Enter radius for circle:'))))

        elif(ch==2):
            def calculate(b,h):
                area=0.5*b*h
                print('Area of triangle is:',area)

            b=int(input('Enter base of triangle:'))
            h=int(input('Enter height of triangle:'))
            calculate(b,h)

        elif(ch==3):
            def calculate(l,b):
                area=l*b
                print('Area of rectangle is:',area)

            l=int(input('Enter length of rectangle:'))
            b=int(input('Enter breadth of rectangle:'))
            calculate(l,b)

        elif(ch==4):
            def calculate(n):
                i=1
                while(i<=n):
                    if(n%i==0):
                        print(i,end=" ")
                    i=i+1

            n=int(input('Enter the number whose factors you need to find:'))
            calculate(n)

        elif(ch==5):
            def calculate(n):
                fac=1
                i=1
                while(i<=n):
                    fac=fac*i
                    i=i+1
                print('Factorial of ',{n},' is:',fac)

            n=int(input('Enter the number whose factorial you need to find:'))
            calculate(n)

        elif(ch==6):
            def calculate(n):
                if(n>1):
                    for i in range(2,n):
                        if(n%i==0):
                            print(n,' is a not prime number')
                            break
                        else:
                            print(n,'is a prime number')
                            break

            n=int(input('Enter a number to check if it is prime:'))
            calculate(n)

        elif(ch==7):
            def calculate(n):
                rev=0
                while(n>0):
                    rem=n%10
                    rev=rev*10+rem
                    n=n//10
                print('Reverese of ',{n},'is:',rev)

            n=int(input('Enter the number you want to reverse:'))
            calculate(n)

        elif(ch==8):
            def calculate(n):
                sum=0
                while(n!=0):
                    sum=sum+n%10
                    n=int(n/10)
                return sum

            n=int(input('Enter any number:'))
            print('Sum of digits is:',calculate(n))

        elif(ch==9):
            def calculate():
                n1=0
                n2=1
                for i in range (0,10):
                    print(n1)
                    n=n1+n2
                    n1=n2
                    n2=n

            print('Fibonacci series:')
            calculate()

        elif(ch==10):
            def calculate(n):
                i=0
                sum=0
                for i in range (1,n):
                    if(n%i==0):
                        sum=sum+i
                if(sum==n):
                    print('The number is a perfect number')
                else:
                    print('It is not a perfect number')

            n=int(input('Enter a number:'))
            calculate(n)

        elif(ch==11):
            def calculate(b,e):
                power=b**e
                print('Output is:',power)

            b=int(input('Enter the value of base:'))
            e=int(input('Enter the value of exponent:'))
            calculate(b,e)

        elif(ch==12):
            def calculate(n):
                sum=0
                temp=n
                i=0
                while(temp!=0):
                    i=temp%10
                    temp=int(temp/10)
                    sum=sum+i**3

                if(sum==n):
                    print('Given number is an armstrong number')
                else:
                    print('Given number is not an armstrong number')

            n=int(input('Enter any number:'))
            calculate(n)

        elif(ch==13):
            def calculate(n):
                rev=0
                rem=0
                temp=n
                while(temp!=0):
                    rem=temp%10
                    rev=rev*10+rem
                    temp=int(temp/10)

                if(rev==n):
                    print('Given number is a palindrome:')
                else:
                    print('Given number is not a palindrome:')

            n=int(input('Enter any number:'))
            calculate(n)

        print('Do you want to continue? press 1')
        ch1=input()
        if(ch1!='1'):
            break
