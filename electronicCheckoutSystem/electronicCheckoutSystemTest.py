from unittest import TestCase
from datetime import datetime
import electronicCheckoutSystem

class TestElectronicCheckoutSystem(TestCase):
    def test_generate_invoice(self):
        actual_invoice = electronicCheckoutSystem.generate_invoice ("John Doe", ["Milk", "Bread"], [2, 3], [10.0, 5.0], 10, "Alice")

        current_date = datetime.now().strftime("%d-%b-%Y %I:%M:%S %p")
        expected_invoice = (
            "\nSEMICOLON STORES\n"
            "MAIN BRANCH\n"
            "LOCATION: 312, HERBERT MACAULAY WAY, SABO YABA, LAGOS.\n"
            "TEL: 0329382343\n"
            f"Date: {current_date}\n"
            f"Cashier: {cashier_name}\n"
            f"Customer Name: {customer_name}\n"
            "===============================================\n"
            f"{'ITEM':<15} {'QTY':<5} {'PRICE':<10} {'TOTAL(NGN)':<10}\n"
            "===============================================\n"
            f"{'Milk':<15} {2:<5} {10.00:<10.2f} {20.00:<10.2f}\n"
            f"{'Bread':<15} {3:<5} {5.00:<10.2f} {15.00:<10.2f}\n"
            "===============================================\n"
            f"Sub Total: {'':>24}{35.00:.2f}\n"
            f"Discount: {'':>24}{3.50:.2f}\n"
            f"VAT @ 7.5%: {'':>22}{2.38:.2f}\n"
            "===============================================\n"
            f"Bill Total: {'':>23}{33.88:.2f}\n"
            "===============================================\n"
            "THIS IS NOT A RECEIPT. KINDLY PAY 33.88"
        )
        self.assertEqual(actual_invoice, expected_invoice)

