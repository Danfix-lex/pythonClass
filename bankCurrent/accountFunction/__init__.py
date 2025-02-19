class AccountFunction:
    def __init__(self, pin, name):
        self.balance = 0
        self.account_exists = True  # Renamed to avoid method conflict
        self.pin = pin
        self.name = name

    def account_exists(self):
        return self.account_exists

    def deposit(self, amount):
        if not self.account_exists:
            raise RuntimeError("Account does not exist")
        if amount < 0:
            raise ValueError("Cannot deposit negative amount")

        self.balance += amount
        return self.balance

    def get_balance(self):
        if not self.account_exists:
            raise RuntimeError("Account does not exist")
        return self.balance

    def withdraw(self, amount, provided_pin):
        if not self.account_exists:
            raise RuntimeError("Account does not exist")
        if amount < 0:
            raise ValueError("Cannot withdraw negative amount")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        if provided_pin != self.pin:
            raise ValueError("Invalid PIN")

        self.balance -= amount
        return self.balance

    def close_account(self):
        self.account_exists = False  # Properly deactivating the account

    def update_pin(self, old_pin, new_pin):
        if old_pin != self.pin:
            raise ValueError("Invalid PIN")
        self.pin = new_pin
        return True
