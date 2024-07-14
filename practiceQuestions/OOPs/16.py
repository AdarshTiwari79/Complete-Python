# Create Account class with 2 attributes- balance & account no.
# Create methods for debit & printing the balance.

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    def debit(self, amount):
        self.balance -= amount
        print("Rs. ",amount, " was debited")
        print("total balance : ",self.getBalance())

    def credit(self, amt):
        self.balance += amt
        print("Rs. ",amt, " was credited")
        print("total balance : ",self.getBalance())

    def getBalance(self):
        return self.balance
        


a = Account(30000,12345)
a.debit(1000)
a.credit(10000)