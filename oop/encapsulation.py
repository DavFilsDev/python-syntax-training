# ENCAPSULATION IN PYTHON

# Encapsulation hides internal details and exposes only what is necessary.

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private variable

    def deposit(self, amount):
        self.__balance += amount

    def show_balance(self):
        print(f"Balance: ${self.__balance}")

account = BankAccount(100)
account.deposit(50)
account.show_balance()

# MEMO:
# - Use __var to make variables private (name mangling).
# - Access private data only via methods.
