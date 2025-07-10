class Transactionsmorethanlimit(Exception):
    def __init__(self, nooftrans, msg="Transactions are more than 6"):
        self.nooftrans = nooftrans
        self.msg = msg

    def __str__(self):
        return f'{self.nooftrans}->{self.msg}'
