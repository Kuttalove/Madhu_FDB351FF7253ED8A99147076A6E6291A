class BankAccount:
    def __init__(self, account_holder, account_number, balance=0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def check_balance(self):
        print(f"Account balance for {self.account_holder}: ${self.balance}")


class SavingsAccount(BankAccount):
    def __init__(self, account_holder, account_number, balance=0, interest_rate=0.03):
        super().__init__(account_holder, account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest_earned = self.balance * self.interest_rate
        self.balance += interest_earned
        print(f"Added interest of ${interest_earned}. New balance: ${self.balance}")

# Example usage
if __name__ == "__main__":
    my_account = SavingsAccount("John Doe", "12345", 1000, 0.05)
    my_account.check_balance()
    my_account.deposit(500)
    my_account.add_interest()
    my_account.check_balance()
    my_account.withdraw(200)
