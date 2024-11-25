from unittest import TestCase
import jessicasStoreFunction

class TestStoreFunction(TestCase):
    def setUp(self):
        self.products = {
            "Laptop": 1000,
            "Phone": 500,
            "Headphones": 100
        }
        self.cart = []
    def test_remove_from_cart_existing_item(self):
        self.cart.append("Laptop")
        result = jessicasStoreFunction.remove_from_cart(self.cart, "Laptop")
        self.assertNotIn("Laptop", self.cart)
        self.assertEqual(result, "Laptop has been removed from your cart.")

    def test_remove_from_cart_nonexistent_item(self):
        result = jessicasStoreFunction.remove_from_cart(self.cart, "Tablet")
        self.assertEqual(result, "Item not found in cart.")

    def test_calculate_total(self):
        self.cart.extend(["Laptop", "Phone", "Headphones"])
        total = jessicasStoreFunction.calculate_total(self.cart, self.products)
        self.assertEqual(total, 1600)

    def test_checkout(self):
        self.cart.extend(["Laptop", "Phone"])
        result = jessicasStoreFunction.checkout(self.cart, self.products)
        self.assertEqual(result, "Thank you for shopping with us! Your total is $1500.")
        self.assertEqual(len(self.cart), 2)

