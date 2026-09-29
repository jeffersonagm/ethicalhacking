class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Fondos insuficientes")
        else:
            self.balance -= amount


account = BankAccount(100)

account.deposit(50)
print("Balance:", account.balance)

account.withdraw(30)
print("Balance:", account.balance)

account.withdraw(200)
print("Balance:", account.balance)