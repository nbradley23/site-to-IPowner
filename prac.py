class BankAccount:
    def __init__ (self, owner, balance = 0.0):
        self.owner = owner
        self.balance = balance
        
    def deposit (self, deposit_amount):
        self.balance += deposit_amount
        return self.balance
    
    def withdraw (self, withdraw_amount):
        self.balance -= withdraw_amount
        return self.balance
    


acct = BankAccount('Darcy')
print(acct.owner) #Darcy
print(acct.balance) #0.0
print(acct.deposit(10))  #10.0
print(acct.withdraw(3))  #7.0
print(acct.balance)   #7.0