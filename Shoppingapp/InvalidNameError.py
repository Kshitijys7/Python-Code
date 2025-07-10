class InvalidNameError(Exception):
    def __init__(self,name,username,msg="Invalid username"):
        self.name=name
        self.username=username
        self.msg=msg

    def __str__(self):
        return f'{self.name}->{self.msg}'

