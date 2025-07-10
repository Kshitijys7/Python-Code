class Address:
    city=""
    state=""
    pin=0

    def acceptAddress(self):
        self.city=input('Enter name of the city:')
        self.state=input('Enter name of the state:')
        self.pin=int(input('Enter PIN number:'))

    def showAddress(self):
        print('City\tState\t\tPin')
        print(f'{self.city}\t{self.state}\t{self.pin}')
