import unittest
from accountFunction import AccountFunction


class AccountTest(unittest.TestCase):

    def setUp(self):
        self.account = AccountFunction(pin=1234, name="Test User")

    def test_deposit(self):
        self.assertEqual(self.account.deposit(1000), 1000)
        self.assertEqual(self.account.deposit(500), 1500)

    def test_deposit_negative(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-100)

    def test_get_balance(self):
        self.account.deposit(2000)
        self.assertEqual(self.account.get_balance(), 2000)

    def test_withdraw_success(self):
        self.account.deposit(3000)
        self.assertEqual(self.account.withdraw(1000, 1234), 2000)

    def test_withdraw_invalid_pin(self):
        self.account.deposit(3000)
        with self.assertRaises(ValueError):
            self.account.withdraw(1000, 9999)

    def test_withdraw_insufficient_funds(self):
        self.account.deposit(1000)
        with self.assertRaises(ValueError):
            self.account.withdraw(2000, 1234)

    def test_withdraw_negative_amount(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(-500, 1234)

    def test_close_account(self):
        self.account.close_account()
        with self.assertRaises(RuntimeError):
            self.account.deposit(1000)

    def test_update_pin_success(self):
        self.assertTrue(self.account.update_pin(1234, 5678))
        with self.assertRaises(ValueError):
            self.account.update_pin(1234, 9999)  # Old PIN is now incorrect

    def test_update_pin_invalid(self):
        with self.assertRaises(ValueError):
            self.account.update_pin(9999, 5678)  # Wrong old PIN


if __name__ == "__main__":
    unittest.main()
