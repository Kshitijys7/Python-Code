class Bill:

    def __init__(self,lstproduct,qty,total,gst,finaltotal):
        self.lstproduct=lstproduct
        self.qty=qty
        self.total=total
        self.gst=gst
        self.finaltotal=finaltotal

    def calculateBill(self):
        for i in self.lstproduct:
            self.total=self.total+i.price*i.qty

        self.gst=0.05*self.total
        self.finaltotal=self.total+self.gst

    def show(self):
        print('Product ID\tProduct Name\tPrice\tQuantity\tTotal')
        for i in self.lstproduct:
            total_item = 0
            total_item = total_item + i.price * i.qty
            print(f'{i.pid}\t\t{i.name}\t\t{i.price}\t\t{i.qty}\t\t{total_item}')

        print('Total Bill-------', self.total)
        print('GST------------', self.gst)
        print('Final Total-----', self.finaltotal)
