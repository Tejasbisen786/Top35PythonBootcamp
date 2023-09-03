class BankAccount:
    def __init__(self, account_holder, initial_balance=0, atm_pin=None):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.atm_pin = atm_pin
        self.transaction_count = 0  # Initialize the transaction count to 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_count += 1
            print(f"Deposited {amount} Rs. New balance: {self.balance}")
            self.check_transaction_count()
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        if self.atm_pin is None:
            print("Transaction PIN is not set. Please set your Transaction PIN.")
            return

        if 0 < amount <= self.balance and self.validate_pin():
            self.balance -= amount
            self.transaction_count += 1
            print(f"Withdrew {amount} Rs. New balance: {self.balance}")
            self.check_transaction_count()
        else:
            print("Invalid withdrawal amount or invalid PIN.")

    def check_balance(self):
        print(f"Current balance for {self.account_holder} is: {self.balance}")

    def validate_pin(self):
        entered_pin = input("Enter your Transaction PIN: ")
        return entered_pin == self.atm_pin

    def check_transaction_count(self):
        if self.transaction_count >= 3:
            print("Congratulations! You've earned 1 credit point.")

    def calculate_interest(self, rate=0.01):
        # Calculate and add interest to the account balance
        interest = self.balance * rate
        self.balance += interest
        print(f"Interest of {interest} Rs added. New balance: {self.balance}")

def main():
    print("Welcome to Our Bank!")
    try:
        account_holder = input("Enter account holder's name: ")
        initial_balance = float(input("Enter initial balance: "))
        atm_pin = input("Set your Transaction PIN: ")
        user_account = BankAccount(account_holder, initial_balance, atm_pin)

        while True:
            print("\nSelect an option:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Calculate Interest")
            print("5. Exit")

            choice = input("Enter option number: ")

            if choice == "1":
                try:
                    amount = float(input("Enter deposit amount: "))
                    user_account.deposit(amount)
                except ValueError:
                    print("Invalid input. Please enter a valid amount.")
            elif choice == "2":
                try:
                    amount = float(input("Enter withdrawal amount: "))
                    user_account.withdraw(amount)
                except ValueError:
                    print("Invalid input. Please enter a valid amount.")
            elif choice == "3":
                user_account.check_balance()
            elif choice == "4":
                user_account.calculate_interest()
            elif choice == "5":
                print("Thank you for using our bank services!")
                break
            else:
                print("Invalid choice. Please select a valid option.")
    except ValueError:
        print("Invalid input. Please enter valid account information.")

if __name__ == "__main__":
    main()
