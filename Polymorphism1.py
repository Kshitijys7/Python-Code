class Instrument:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def show(self):
         print(self.x,'',self.y)

class Guitar(Instrument):
    pass

class Piano(Instrument):
    pass

#Guitar.show("Guitar","tantantan")
