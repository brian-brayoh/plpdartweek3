from abc import ABC, abstractmethod  # Importing Abstract Base Classes module

# Encapsulation: Superclass with private variables
class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # Private variable
        self.__balance = balance  # Private variable
    
    # Getter for account number
    def get_account_number(self):
        return self.__account_number

    # Getter for balance
    def get_balance(self):
        return self.__balance

    # Setter for balance
    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Invalid balance amount")

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive")

    # Abstract method for withdrawing money (Abstraction)
    @abstractmethod
    def withdraw(self, amount):
        pass


# Inheritance: Subclass that inherits from BankAccount and implements withdraw
class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate  # Additional property

    # Polymorphism: Implement withdraw method
    def withdraw(self, amount):
        if 0 < amount <= self.get_balance():
            self.set_balance(self.get_balance() - amount)
            print(f"Withdrew {amount}. New balance: {self.get_balance()}")
        else:
            print("Insufficient balance or invalid amount")


# Another Subclass demonstrating Polymorphism by overriding withdraw
class CurrentAccount(BankAccount):
    def __init__(self, account_number, balance, overdraft_limit):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit  # Additional property

    # Polymorphism: Implement withdraw method differently
    def withdraw(self, amount):
        if amount <= self.get_balance() + self.overdraft_limit:
            self.set_balance(self.get_balance() - amount)
            print(f"Withdrew {amount}. New balance: {self.get_balance()}")
        else:
            print("Exceeds overdraft limit")

# Testing the implementation

# Create instances of SavingsAccount and CurrentAccount
savings = SavingsAccount(account_number="SA12345", balance=1000, interest_rate=0.05)
current = CurrentAccount(account_number="CA54321", balance=500, overdraft_limit=300)

# Access encapsulated data using getters
print(f"Savings Account Number: {savings.get_account_number()}")
print(f"Current Account Balance: {current.get_balance()}")

# Perform deposits and withdrawals
savings.deposit(500)
savings.withdraw(200)

current.withdraw(700)  # Within overdraft limit
current.withdraw(200)  # Exceeds overdraft limit
