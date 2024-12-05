from unittest import TestCase
import atmAppFuntion

class TestAtmAppFunction(TestCase):
    def test_deposit_money(self):
        initial_balance = atmAppFunction.account_balances[0]
        deposit_amount = atmAppFunction.deposit_money(0, 100.0)
        self.assertEqual(deposit_amount, 100.0)
        self.assertEqual(atmAppFunction.account_balances[0], initial_balance + 100.0)

    def test_withdraw_money(self):
        atmAppFunction.deposit_money(0, 100.0) 
        withdrawn_amount = atmAppFunction.withdraw_money(0, 50.0)
        self.assertEqual(withdrawn_amount, 50.0)
        self.assertEqual(atmAppFunction.account_balances[0], 150.0)
        insufficient_funds = atmAppFunction.withdraw_money(0, 500.0)
        self.assertEqual(insufficient_funds, -1)

    def test_transfer_money(self):
        atmAppFunction.deposit_money(0, 100.0)
        transfer_amount = atmAppFunction.transfer_money(0, 50.0)
        self.assertEqual(transfer_amount, 50.0)
        self.assertEqual(atmAppFunction.account_balances[0], 50.0)
        invalid_transfer = atmAppFunction.transfer_money(0, 500.0)
        self.assertEqual(invalid_transfer, -1)
