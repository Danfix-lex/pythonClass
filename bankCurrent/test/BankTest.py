import unittest
from bankFunction import BankFunction


class BankTest(unittest.TestCase):
    def setUp(self):
        self.bank = BankFunction()

    def test_create_account(self):
        self.assertTrue(self.bank.create_account(1234, 1, "Samuel"))
        self.assertTrue(self.bank.create_account(5678, 2, "Tunde"))
        self.assertFalse(self.bank.create_account(1234, 1, "Bisola"))
        self.assertFalse(self.bank.create_account(2345, 3, "Dele"))

    def test_deposit(self):
        self.bank.create_account(1234, 1, "Samuel")
        self.assertTrue(self.bank.deposit(1000, 1))
        self.assertTrue(self.bank.deposit(500, 1))
        self.assertFalse(self.bank.deposit(500, 3))

    def test_withdraw(self):
        self.bank.create_account(1234, 1, "Samuel")
        self.bank.deposit(1000, 1)
        self.assertTrue(self.bank.withdraw(500, 1234, 1))
        self.assertFalse(self.bank.withdraw(1500, 1234, 1))
        self.assertFalse(self.bank.withdraw(500, 1111, 1))
        self.assertFalse(self.bank.withdraw(500, 1234, 3))

    def test_transfer(self):
        self.bank.create_account(1234, 1, "Samuel")
        self.bank.create_account(5678, 2, "Tunde")
        self.bank.deposit(1000, 1)
        self.assertTrue(self.bank.transfer(500, 1234, 1, 2))
        self.assertFalse(self.bank.transfer(1500, 1234, 1, 2))
        self.assertFalse(self.bank.transfer(500, 1111, 1, 2))
        self.assertFalse(self.bank.transfer(500, 1234, 1, 3))

    def test_close_account(self):
        self.bank.create_account(1234, 1, "Samuel")
        self.assertTrue(self.bank.close_account(1))
        self.assertFalse(self.bank.close_account(1))
        self.assertFalse(self.bank.close_account(3))

    def test_invalid_operations(self):
        self.assertFalse(self.bank.deposit(1000, 3))
        self.assertFalse(self.bank.withdraw(500, 1234, 3))
        self.assertFalse(self.bank.transfer(500, 1234, 1, 3))


if __name__ == '__main__':
    unittest.main()
