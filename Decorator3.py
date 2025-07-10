def Greater(func):
    def inner(n1,n2):
        if type(n1)==int and type(n2)==int:
            if int(n1) > int(n2):
                # print('Greater number is:',n1)
                return n1

            else:
                # print('Greater number is:', n2)
                return n2

        elif type(n1)==float and type(n2)==float:
            if float(n1) > float(n2):
                # print('Greater number is:',n1)
                return n1

            else:
                # print('Greater number is:', n2)
                return n2

        else:
            if int(ord(n1))>int(ord(n2)):
                #print('Greater number is:',n1)
                return n1

            else:
                #print('Greater number is:', n2)
                return n2
    return inner


@Greater
def Numbers(n1,n2):
    ans=n1
    return ans


print(Numbers(2,4))
print(Numbers(2.2,4.2))
print(Numbers('a','c'))
