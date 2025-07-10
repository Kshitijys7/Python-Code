def calc_area1(r):
    area = 3.14 * r * r
    print('Area of circle is:', area)


def calc_area2(b, h):
    area = 0.5 * b * h
    print('Area of triangle is:', area)


def calc_area3(l, b):
    area = l * b
    print('Area of rectangle is:', area)


def factors(n):
    i = 1
    while (i <= n):
        if (n % i == 0):
            print(i, end=" ")
        i = i + 1


def factorial(n):
    fac = 1
    i = 1
    while (i <= n):
        fac = fac * i
        i = i + 1
    print('Factorial of ', {n}, ' is:', fac)


def prime(n):
    if (n > 1):
        for i in range(2, n):
            if (n % i == 0):
                print(n, ' is a not prime number')
                break
            else:
                print(n, 'is a prime number')
                break


def reverse(n):
    rev=0
    while(n>0):
        rem=n%10
        rev=rev*10+rem
        n=n//10
    print('Reverese of ',{n},'is:',rev)


def sumofdigits(n):
    sum = 0
    while (n != 0):
        sum = sum + n % 10
        n = int(n / 10)
    print('Sum of digits is:',sum)


def fibonacci():
    n1 = 0
    n2 = 1
    for i in range(0, 10):
        print(n1)
        n = n1 + n2
        n1 = n2
        n2 = n


def perfectno(n):
    i = 0
    sum = 0
    for i in range(1, n):
        if (n % i == 0):
            sum = sum + i
    if (sum == n):
        print('The number is a perfect number')
    else:
        print('It is not a perfect number')


def power(b, e):
    power = b ** e
    print('Output is:', power)


def armstrong(n):
    sum = 0
    temp = n
    i = 0
    while (temp != 0):
        i = temp % 10
        temp = int(temp / 10)
        sum = sum + i ** 3

    if (sum == n):
        print('Given number is an armstrong number')
    else:
        print('Given number is not an armstrong number')


def palindrome(n):
    rev = 0
    rem = 0
    temp = n
    while (temp != 0):
        rem = temp % 10
        rev = rev * 10 + rem
        temp = int(temp / 10)

    if (rev == n):
        print('Given number is a palindrome:')
    else:
        print('Given number is not a palindrome:')

def pattern1(n):
    for i in range(0, n):
        for j in range(0, i + 1):
            print('*', end=" ")
        print('\n')

def pattern2(n):
    for i in range(0, n):
        for j in range(n - i, 0, -1):
            print('* ', end=" ")
        print('\n')

def pattern3(n):
    for i in range(0, n // 2):
        print('* ' * i)
    for i in range((n // 2) - 1, 0, -1):
        print('* ' * i)
    print('\n')

def pattern4(n):
    k = 2 * n - 2

    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 1

        for j in range(0, i + 1):
            print('* ', end=" ")
        print('\n')

def num_pattern1(n):
    num = 1
    for i in range(0, n):
        for j in range(0, i + 1):
            print(num, end=" ")
            num = num + 1
        print('\n')

def num_pattern2(n):
    num = 1

    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            print(num, end=" ")
            num = num + 1
        num = 1
        print('\n')

def alph_pattern(n):
    num = 65

    for i in range(0, n):
        for j in range(0, i + 1):
            print(chr(num), end=" ")
            num = num + 1
        print("\n")

while(True):
    print('1.Area\n2.Logic\n3.Patterns')
    ch=int(input('Enter your choice:'))

    if(ch==1):
        while(True):
            print('1.Circle\n2.Triangle\n3.Rectangle')
            ch1=int(input('Enter your choice:'))


            if(ch1==1):
                print(calc_area1(int(input('Enter radius for circle:'))))

            elif(ch1==2):
                b=int(input('Enter base for triangle:'))
                h=int(input('Enter height for triangle:'))
                calc_area2(b,h)

            elif(ch1==3):
                l=int(input('Enter length for rectangle:'))
                b=int(input('Enter breadth for rectangle:'))
                calc_area3(l,b)

            else:
                print('Invalid choice')

            print('Do you want to continue with areas? press 1 otherwise press any key')
            choice1 = input()
            if (choice1 != '1'):
                break


    elif(ch==2):
        while (True):
            print('1.Factors\n2.Factorial\n3.Prime number\n4.Reverse\n5.Sum of digits\n6.Fibonacci series\n7.Perfect number\n8.Power\n9.Armstrong number\n10.Palindrome number')
            ch2 = int(input('Enter your choice:'))

            if(ch2==1):
                print(factors(int(input('Enter number for which you want to find factors:'))))

            elif(ch2==2):
                print(factorial(int(input('Enter number whose factorial you want to find:'))))

            elif(ch2==3):
                print(prime(int(input('Enter any number:'))))

            elif(ch2==4):
                print(reverse(int(input('Enter any number to reverse:'))))

            elif(ch2==5):
                print(sumofdigits(int(input('Enter any number:'))))

            elif(ch2==6):
                print(fibonacci())

            elif(ch2==7):
                print(perfectno(int(input('Enter any number:'))))

            elif(ch2==8):
                b=int(input('Enter a base:'))
                e=int(input('Enter an exponent:'))
                power(b,e)

            elif(ch2==9):
                print(armstrong(int(input('Enter any number:'))))

            elif(ch2==10):
                print(palindrome(int(input('Enter any number:'))))

            else:
                print('Invalid choice')

            print('Do you want to continue with logics? press 1 otherwise press any key')
            choice2 = input()
            if (choice2 != '1'):
                break

    elif(ch==3):
        while(True):
            print('1.Star pattern\n2.Inverted star pattern\n3.Increasing and decreasing star pattern\n4.Pascal Triangle\n5.Continuous number pattern\n6.Decreasing number pattern\n7.Alphabet pattern')
            ch3=int(input('Enter your choice:'))

            if(ch3==1):
                print(pattern1(int(input('Enter number of rows you want:'))))

            elif(ch3==2):
                print(pattern2(int(input('Enter number of rows you want:'))))

            elif(ch3==3):
                print(pattern3(int(input('Enter number of rows you want:'))))

            elif(ch3==4):
                print(pattern4(int(input('Enter number of rows you want:'))))

            elif(ch3==5):
                print(num_pattern1(int(input('Enter number of rows you want:'))))

            elif(ch3==6):
                print(num_pattern2(int(input('Enter number of rows you want:'))))

            elif(ch3==7):
                print(alph_pattern(int(input('Enter number of rows you want:'))))

            print('Do you want to continue with patterns? press 1 otherwise press any key')
            choice3 = input()
            if (choice3 != '1'):
                break

    else:
        print('Invalid choice:')

    print('Do you want to continue on main menu? press 1 otherwise press any key to exit')
    choice=input()
    if(choice!='1'):
        break