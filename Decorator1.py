def outer(func):
    def inner(a):
        if a<0:
            a=a*(-1)
        return a
    return inner

@outer
def numbers(a):
    ans=a
    return ans


print(numbers(-4))
'''outer1=outer(numbers)
print(numbers(-1))
outer1(-1)
'''

