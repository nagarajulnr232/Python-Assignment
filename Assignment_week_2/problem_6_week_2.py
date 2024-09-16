## Implement a simple ATM program that allows a user to withdraw money based on their balance.

class bank_account:
    def __init__(self,balance):
        self.balance=balance

    def withdraw(self,amount):
        if 0<amount<self.balance:
            self.balance-=amount
            print("Withdrawl is",amount)
        else:
            print('''Sorry ! Insufficient funds in your account..''')
    def get_balance(self):
        return self.balance
account=bank_account(5000)
print("Total Balance",account.get_balance())
account.withdraw(1000)
print("Available balance:",account.get_balance())