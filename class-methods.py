class BankAccount:
    def __init__ (self, owner):
        self.owner = owner
        self.balance = 0.0
        
    def deposit (self, deposit_amount):
        self.balance += deposit_amount
        return self.balance
    
    def withdraw (self, withdraw_amount):
        self.balance -= withdraw_amount
        return self.balance
    


acct = BankAccount('Nick')
print(acct.owner) #Nick
print(acct.balance) #0.0
print(acct.deposit(10))  #10.0
print(acct.withdraw(3))  #7.0
print(acct.balance)   #7.0