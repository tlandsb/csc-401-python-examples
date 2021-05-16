class Account(object):
    'a better bank account class (version 2)'
    bankName = "Citibank" #an instance variable

    def __init__(self,custName='unknown', idNum=-1, bal=None,intRate=None):
        '''constructor for Account class, balance must be in decimal form'''
        self.name = custName
        self.custId = idNum
        self.balance = bal
        self.rate = intRate

    def deposit(self, amount):
        'adds amount to balance'
        self.balance += amount

    def withdraw(self,withdrawalAmount):
        '''deducts withdrawalAmount from balance
        requires that balance >= withdrawalAmount
        returns -1 if not, and does not adjust balance'''

        if self.balance>=withdrawalAmount:
            self.balance = self.balance - withdrawalAmount
        else:
            #perhaps print error message to log
            return -1

    def setInterest(self,newRate):
        '''changes rate to newRate
        rate must be in decimal form (e.g. 0.05)'''
        self.rate = newRate

    def addInterest(self):
        '''updates balance by adding interest to it, requires rate to be set'''
        self.balance = self.balance + (self.balance*self.rate)

    def __str__(self):
        'returns a nicely formatted string representation of the object'
        
        s = 'Name:\t{}\n\
ID: \t{}\n\
Balance: ${}\n\
Interest Rate: {}%'.format(self.name,self.custId,self.balance,self.rate*100)
        return s
s1=Account(custName='tom', idNum=-1, bal=1200,intRate=.5)
s1.withdraw(10)
print(s1)

