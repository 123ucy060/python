#hi new update 
#encapsulation (safe )           access only inside the class

class BankAccount:
    def __init__(self):
        self.__balance = 0                  # private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive")

    def get_balance(self):
        return self.__balance


# ---- PROGRAM EXECUTION ----

# Create a bank account object
account = BankAccount()

# Deposit money
account.deposit(500)
account.deposit(300)

# Check balance
print("Current Balance:", account.get_balance())








