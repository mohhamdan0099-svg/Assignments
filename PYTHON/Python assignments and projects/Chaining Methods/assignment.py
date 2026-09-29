class User:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance

    def make_deposits(self,amount):
        self.balance+=amount
        return self

    def make_withdrawal(self,amount):
        self.balance-=amount
        return self

    def transfer_money(self, other_user, amount):
        self.balance-=amount
        other_user.balance+=amount
        return self

    def display_user_balance(self):
        print(f"{self.name}, Balance:{self.balance}")   
        return self



first_user = User("Guido van Rossum",150)
second_user =User("yousef", 1000)
third_user = User("Bashar",1)

first_user.display_user_balance().make_deposits(30).make_deposits(20).make_deposits(10).display_user_balance().make_withdrawal(10).display_user_balance()

second_user.display_user_balance().make_deposits(150).make_deposits(200).display_user_balance().make_withdrawal(100).make_withdrawal(100).display_user_balance()

third_user.display_user_balance().make_deposits(150).display_user_balance().make_withdrawal(100).make_withdrawal(100).make_withdrawal(100).display_user_balance()

first_user.transfer_money(third_user,50).display_user_balance()

third_user.display_user_balance()