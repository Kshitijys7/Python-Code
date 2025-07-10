def outer(func):
    def inner(str,cnt):
        element='A,a,E,e,I,i,O,o,U,u'
        for i in str:
            if i in element:
                cnt=cnt+1
        return cnt
    return inner


@outer
def inputString(str,cnt):
    ans=cnt
    return ans

print(inputString('hello',0))

