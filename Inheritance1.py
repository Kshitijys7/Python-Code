class Base1:
    def __init__(self):
        print('hi')
    def show1(self):
        print('Base1')

class Base2:
    def __init__(self):
        print('hello')
    def show1(self):
        print('Base2')

class derived1(Base1,Base2):
    def __init__(self):
        super().__init__()
        print('Derived...')

    def show(self):
        Base1.show1(self)
        Base2.show1(self)
        print('Derived.....')

d1=derived1()
d1.show()
d1.show1()
print('Check',issubclass(derived1,Base1))
print(isinstance(d1,derived1))
print(isinstance(d1,object))
print(isinstance(d1,Base1))