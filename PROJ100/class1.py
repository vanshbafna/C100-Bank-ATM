class ATM(object):

    def __init__(self,company,Transaction_limit):
        self.company = company
        self.Transaction_limit = Transaction_limit
    
    def amount(self):
        print("Amount = 24000rs")

    def Debited(self):
        print("Debited")
    
Axis = ATM("Axis",80000)

print(Axis.amount())
print(Axis.Debited())
