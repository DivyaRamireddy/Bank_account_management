# bank_oops.py
# OOP-based Bank Account System

from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, name, balance=0):
        self._name = name          # encapsulation
        self._balance = balance

    @abstractmethod
    def calculate_interest(self):
        pass

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited ₹{amount}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdrawn ₹{amount}")
        else:
            print("Insufficient balance")

    def show_balance(self):
        print(f"Current Balance: ₹{self._balance}")


class SavingsAccount(BankAccount):
    def calculate_interest(self):
        interest = self._balance * 0.04
        self._balance += interest
        print(f"Interest added: ₹{interest}")


class CurrentAccount(BankAccount):
    def calculate_interest(self):
        print("No interest for current account")


if __name__ == "__main__":
    print("🏦 Bank Account System")

    acc1 = SavingsAccount("Divya", 5000)
    acc1.deposit(2000)
    acc1.calculate_interest()
    acc1.show_balance()

    print()

    acc2 = CurrentAccount("Reddy", 8000)
    acc2.withdraw(3000)
    acc2.calculate_interest()
    acc2.show_balance()
