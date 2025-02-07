class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number   # Encapsulating the account number
        self.__balance = balance                 # Encapsulating the balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposit of {amount} INR successful. New balance: {self.__balance} INR"
        return "Invalid deposit amount!"

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrawal of {amount} INR successful. Remaining balance: {self.__balance} INR"
        return "Invalid withdrawal amount or insufficient funds."

    def get_balance(self):
        return f"Your balance is {self.__balance} INR"

# Encapsulation protects the balance and account number
account = BankAccount("123456789", 5000)
print(account.deposit(1000))
print(account.withdraw(3000))
print(account.get_balance())

# Trying to access or modify private attributes directly will fail
# print(account.__balance)   # Raises AttributeError because it's encapsulated
