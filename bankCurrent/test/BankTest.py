import unittest
from bankFunction import BankFunction


class BankTest(unittest.TestCase):
    def setUp(self):
        self.bank = BankFunction()

    def test_create_account(self):
        # Test for account creation
        self.assertTrue(self.bank.create_account(1234, 1, "Alice"))
        self.assertTrue(self.bank.create_account(5678, 2, "Bob"))
        self.assertFalse(self.bank.create_account(1234, 1, "Charlie"))  # Account 1 already exists
        self.assertFalse(self.bank.create_account(2345, 3, "Charlie"))  # Invalid account number

    def test_deposit(self):
        # Create account and test deposit
        self.bank.create_account(1234, 1, "Alice")
        self.assertTrue(self.bank.deposit(1000, 1))  # Valid deposit
        self.assertFalse(self.bank.deposit(-500, 1))  # Invalid deposit (negative amount)
        self.assertFalse(self.bank.deposit(500, 3))  # Account 3 doesn't exist

    def test_withdraw(self):
        # Create account and test withdrawal
        self.bank.create_account(1234, 1, "Alice")
        self.bank.deposit(1000, 1)
        self.assertTrue(self.bank.withdraw(500, 1234, 1))  # Valid withdrawal
        self.assertFalse(self.bank.withdraw(1500, 1234, 1))  # Insufficient funds
        self.assertFalse(self.bank.withdraw(500, 1111, 1))  # Invalid PIN
        self.assertFalse(self.bank.withdraw(500, 1234, 3))  # Account 3 doesn't exist

    def test_transfer(self):
        # Create accounts and test transfer
        self.bank.create_account(1234, 1, "Alice")
        self.bank.create_account(5678, 2, "Bob")
        self.bank.deposit(1000, 1)
        self.assertTrue(self.bank.transfer(500, 1234, 1, 2))  # Valid transfer
        self.assertFalse(self.bank.transfer(1500, 1234, 1, 2))  # Insufficient funds
        self.assertFalse(self.bank.transfer(500, 1111, 1, 2))  # Invalid PIN
        self.assertFalse(self.bank.transfer(500, 1234, 1, 3))  # Account 3 doesn't exist

    def test_close_account(self):
        # Create account and test account closure
        self.bank.create_account(1234, 1, "Alice")
        self.assertTrue(self.bank.close_account(1))  # Account 1 closed successfully
        self.assertFalse(self.bank.close_account(1))  # Account 1 is already closed
        self.assertFalse(self.bank.close_account(3))  # Account 3 doesn't exist

    def test_invalid_operations(self):
        # Try invalid operations on non-existent accounts
        self.assertFalse(self.bank.deposit(1000, 3))  # Account 3 doesn't exist
        self.assertFalse(self.bank.withdraw(500, 1234, 3))  # Account 3 doesn't exist
        self.assertFalse(self.bank.transfer(500, 1234, 1, 3))  # Account 3 doesn't exist


if __name__ == '__main__':
    unittest.main()
