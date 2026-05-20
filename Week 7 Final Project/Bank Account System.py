# ================================================
# File: Bank_Account_System.py
# Topic: OOP Project – Bank Account Management System
# ================================================

"""
A simple Bank Account System using Python OOP concepts.
Features:
- Deposit, Withdraw, Balance Inquiry
- Encapsulation with private balance
- Input validation and error handling
"""

# ---------------------------
#  BankAccount Class
# ---------------------------
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"✅ {amount} deposited successfully. New Balance: {self.__balance}")
        else:
            print("❌ Deposit amount must be greater than 0.")

    def withdraw(self, amount):
        if amount <= 0:
            print("❌ Withdrawal amount must be greater than 0.")
        elif amount > self.__balance:
            print("❌ Insufficient balance!")
        else:
            self.__balance -= amount
            print(f"✅ {amount} withdrawn successfully. Remaining Balance: {self.__balance}")

    def check_balance(self):
        print(f"💰 Current Balance: {self.__balance}")

    def get_balance(self):
        return self.__balance

    def __str__(self):
        return f"Account Holder: {self.account_holder}, Balance: {self.__balance}"


# ---------------------------
#  Main Program
# ---------------------------
def main():
    print("=== Welcome to the Bank Account System ===")
    name = input("Enter account holder name: ")
    account = BankAccount(name)

    while True:
        print("\nSelect an option:")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Account Info")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == "3":
            account.check_balance()
        elif choice == "4":
            print(account)
        elif choice == "5":
            print("Thank you for using the Bank Account System. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")


# ---------------------------
#  Run the Program
# ---------------------------
if __name__ == "__main__":
    main()