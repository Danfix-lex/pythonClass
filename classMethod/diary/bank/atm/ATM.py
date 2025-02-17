class ATM:
    def __init__(self, pin, name):
        self.balance = 0
        self.it_exist = True
        self.pin = pin
        self.name = name

    def it_exist(self):
        return self.it_exist

    def deposit(self, amount):
        if not self.it_exist:
            raise RuntimeError("Account does not exist")
        elif amount < 0:
            raise ValueError("Cannot deposit negative amount")
        else:
            self.balance += amount
            return self.balance

    def get_balance(self):
        if not self.it_exist:
            raise RuntimeError("Account does not exist")
        else:
            return self.balance

    def withdraw(self, amount, provided_pin):
        if not self.it_exist:
            raise RuntimeError("Account does not exist")
        elif amount < 0:
            raise ValueError("Cannot withdraw negative amount")
        elif amount > self.balance:
            raise ValueError("Insufficient funds")
        elif provided_pin is not None and provided_pin == self.pin:
            self.balance -= amount
            return self.balance
        else:
            raise ValueError("Invalid PIN")

    def does_not_exist(self):
        self.it_exist = False
        return False

    def update_pin(self, pin, new_pin):
        if pin != self.pin:
            raise ValueError("Invalid PIN")
        else:
            self.pin = new_pin
            return True

class ATM:
    def __init__(self, bank):
        self.bank = bank

    def atm_menu(self):
        while True:
            option_str = input(
                """Welcome to the ATM
                1. Create Account
                2. Deposit
                3. Withdraw
                4. Transfer
                5. Check Balance
                6. Close Account
                7. Exit
                Select an option: """
            )
            try:
                option = int(option_str)
                self.process_option(option)
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def process_option(self, option):
        if option == 1:
            self.create_account()
        elif option == 2:
            self.deposit()
        elif option == 3:
            self.withdraw()
        elif option == 4:
            self.transfer()
        elif option == 5:
            self.check_balance()
        elif option == 6:
            self.close_account()
        elif option == 7:
            print("Thank you for using the ATM. Goodbye!")
            exit()
        else:
            print("Invalid option. Please try again.")

    def create_account(self):
        try:
            account_number = int(input("Enter account number (1 or 2): "))
            pin = input("Enter PIN: ")
            name = input("Enter Name: ")
            self.bank.create_account(pin, account_number, name)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def deposit(self):
        try:
            account_number = int(input("Enter account number: "))
            amount = int(input("Enter amount to deposit: "))
            self.bank.deposit(amount, account_number)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def withdraw(self):
        try:
            account_number = int(input("Enter account number: "))
            pin = input("Enter PIN: ")
            amount = int(input("Enter amount to withdraw: "))
            self.bank.withdraw(amount, pin, account_number)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def transfer(self):
        try:
            from_account = int(input("Enter sender account number: "))
            to_account = int(input("Enter receiver account number: "))
            pin = input("Enter PIN: ")
            amount = int(input("Enter amount to transfer: "))
            self.bank.transfer(amount, pin, from_account, to_account)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def check_balance(self):
        try:
            account_number = int(input("Enter account number: "))
            account = self.bank.get_account(account_number)
            if account:
                print(f"Your balance is: {account.get_balance()}")
            else:
                print("Account does not exist.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def close_account(self):
        try:
            account_number = int(input("Enter account number to close: "))
            self.bank.close_account(account_number)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    bank_function = None  # Replace with actual bank function implementation
    atm = ATM(bank_function)
    atm.atm_menu()
