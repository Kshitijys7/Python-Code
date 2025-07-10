class Balancelessthanlimit(Exception):
    def __init__(self, bal, msg="Balance is less than 1000"):
        self.bal = bal
        self.msg = msg

    def __str__(self):
        return f'{self.bal}->{self.msg}'
