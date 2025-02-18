class AccountFunction:
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
