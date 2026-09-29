class BankAccount:
    def __init__(self):
        self.int_rate = 0.01
        self.balance =  1000


    def deposit(self, amount):
        self.balance+=amount
        return self


    def withdrawl(self, amount):
        if self.balance> 0:
            self.balance-=amount
        else:
            print("Insufficient funds:Charging a $5 fee" )
            self.balance-=5
        return self    
        
    def display_account_info(self):
        print(f"Balance:{self.balance}")
        return self

    
    def yield_interest(self):
        if self.balance>0:
            self.balance=self.balance+(self.balance)*self.int_rate
        return self
        

account_one= BankAccount()
account_two=BankAccount()

account_one.deposit(100).deposit(100).deposit(100). withdrawl(200).yield_interest().display_account_info()
account_two.deposit(100).deposit(100).withdrawl(200).withdrawl(200).withdrawl(200).withdrawl(200).yield_interest().display_account_info()