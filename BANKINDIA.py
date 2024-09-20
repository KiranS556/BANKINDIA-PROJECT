class BankAccount:
    def __init__(self, account_number, password):
        self.account_number = account_number
        self.password = password
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def check_balance(self):
        print(f"Current balance: {self.balance}")

class BankSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, password):
        if account_number not in self.accounts:
            self.accounts[account_number] = BankAccount(account_number, password)
            print(f"Account {account_number} created successfully.")
        else:
            print("Account already exists.")

    def login(self, account_number, password):
        account = self.accounts.get(account_number)
        if account and account.password == password:
            print("Login successful.")
            return account
        else:
            print("Invalid account number or password.")
            return None

def main():
    bank_system = BankSystem()
    while True:
        print("\nWelcome to BANKINDIA Menu:")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            account_number = input("Enter account number: ")
            password = input("Enter password: ")
            bank_system.create_account(account_number, password)
        elif choice == '2':
            account_number = input("Enter account number: ")
            password = input("Enter password: ")
            account = bank_system.login(account_number, password)
            if account:
                while True:
                    print("\nAccount Menu:")
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Check Balance")
                    print("4. Logout")
                    account_choice = input("Choose an option: ")

                    if account_choice == '1':
                        amount = float(input("Enter amount to deposit: "))
                        account.deposit(amount)
                    elif account_choice == '2':
                        amount = float(input("Enter amount to withdraw: "))
                        account.withdraw(amount)
                    elif account_choice == '3':
                        account.check_balance()
                    elif account_choice == '4':
                        print("Logged out.")
                        break
                    else:
                        print("Invalid option. Please try again.")
        elif choice == '3':
            print("Thank you for using BANKINDIA. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
