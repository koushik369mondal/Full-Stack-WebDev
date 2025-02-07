class ATM:
    def __init__(self, balance):
        self.balance = balance

    def check_balance(self):
        return f"Your balance is: {self.balance} INR"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance!"
        else:
            self.balance -= amount
            return f"Withdrawal successful! Remaining balance: {self.balance} INR"
    
    def deposit(self, amount):
        self.balance += amount
        return f"Deposit successful! New balance: {self.balance} INR"

# Abstracting the internal complexities, user interacts with only these simple methods
atm = ATM(5000)
print(atm.check_balance())   # Checking balance
print(atm.withdraw(1000))    # Withdrawing money
print(atm.deposit(1500))     # Depositing money
