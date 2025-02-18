class BankFunction:
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
        return False

    def get_account(self, account_number):
        if account_number == 1:
            print(f"This is your account: {account_number}")
            return self.account1
        elif account_number == 2:
            print(f"This is your account: {account_number}")
            return self.account2
        return None

    def deposit(self, amount, account_number):
        account = self.get_account(account_number)
        if account:
            account.deposit(amount)
            print(f"₦{amount} has been deposited successfully")
            return True
        return False

    def withdraw(self, amount, pin, account_number):
        account = self.get_account(account_number)
        if account:
            print(f"₦{amount} has been withdrawn successfully")
            return account.withdraw(amount, pin) >= 0
        return False

    def transfer(self, amount, pin, from_account, to_account):
        sender = self.get_account(from_account)
        receiver = self.get_account(to_account)
        if sender and receiver and sender.withdraw(amount, pin) >= 0:
            receiver.deposit(amount)
            print(f"₦{amount} has been transferred successfully from {from_account} to {to_account}")
            return True
        return False

    def close_account(self, account_number):
        if account_number == 1 and self.account1:
            self.account1 = None
            print(f"Account: {account_number} has been closed successfully")
            return True
        elif account_number == 2 and self.account2:
            self.account2 = None
            print(f"Account: {account_number} has been closed successfully")
            return True
        return False
