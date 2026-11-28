class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def display(self):
        print("Account Holder:", self.name)
        print("Balance:", self.balance)

b1 = Bank("Priya", 50000)
b1.display()
