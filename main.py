# 1
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposidt(self, amount):
            self.balance += amount
            print(f"{amount} summa balansga qoshildi")

    def withdraw(self, amount):
        self.balance -= amount
        print(f"{amount} summa balnisdan yechildi")

    def info(self):
        print(f"egasi: {self.owner}, balansi: {self.balance}")

u1 = BankAccount("Aziz", 100000)
u1.info()


u1.deposidt(70000)
u1.info()

u1.withdraw(50000)
u1.info()
