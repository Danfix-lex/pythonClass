class AccountFunction:
    def __init__(self, pin, name):
        self.balance = 0
        self.pin = pin
        self.name = name

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Cannot deposit negative amount")
        self.balance += amount
        return self.balance

    def get_balance(self):
        return self.balance

    def withdraw(self, amount, provided_pin):
        if provided_pin != self.pin:
            raise ValueError("Invalid PIN")
        if amount < 0:
            raise ValueError("Cannot withdraw negative amount")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        return self.balance


class BankFunction:
    def __init__(self):
        self.account1 = None
        self.account2 = None

    def create_account(self, pin, account_number, name):
        if account_number == 1 and self.account1 is None:
            self.account1 = AccountFunction(pin, name)
            print(f"Account: {account_number} has been created successfully")
            return True
        elif account_number == 2 and self.account2 is None:
            self.account2 = AccountFunction(pin, name)
            print(f"Account: {account_number} has been created successfully")
            return True
        print("Account creation failed: Account already exists or invalid account number.")
        return False

    def get_account(self, account_number):
        if account_number == 1:
            return self.account1
        elif account_number == 2:
            return self.account2
        print("Account not found.")
        return None

    def deposit(self, amount, account_number):
        account = self.get_account(account_number)
        if account:
            account.deposit(amount)
            print(f"₦{amount} has been deposited successfully")
            return True
        print(f"Account {account_number} does not exist.")
        return False

    def withdraw(self, amount, pin, account_number):
        account = self.get_account(account_number)
        if account:
            try:
                account.withdraw(amount, pin)
                print(f"₦{amount} has been withdrawn successfully from account {account_number}")
                return True
            except ValueError as e:
                print(e)
        print(f"Account {account_number} does not exist or withdrawal failed.")
        return False

    def transfer(self, amount, pin, from_account, to_account):
        sender = self.get_account(from_account)
        receiver = self.get_account(to_account)
        if sender and receiver:
            try:
                sender.withdraw(amount, pin)
                receiver.deposit(amount)
                print(f"₦{amount} has been transferred successfully from {from_account} to {to_account}")
                return True
            except ValueError as e:
                print(e)
        print("Transfer failed: Either source or destination account does not exist or insufficient funds.")
        return False

    def close_account(self, account_number):
        if account_number == 1 and self.account1:
            self.account1 = None
            print(f"Account {account_number} has been closed successfully")
            return True
        elif account_number == 2 and self.account2:
            self.account2 = None
            print(f"Account {account_number} has been closed successfully")
            return True
        print(f"Account {account_number} does not exist or already closed.")
        return False
