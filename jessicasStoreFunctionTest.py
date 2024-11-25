from unittest import TestCase
import jessicasStoreFunction

class TestJessicasStoreFunction(TestCase):
    def setUp(self):
        self.products = {
            "Laptop": 1000,
            "Phone": 500,
            "Headphones": 100
        }
        self.cart = []

    def test_add_to_cart_existing_product(self):
        actual = jessicasStoreFunction.add_to_cart(self.cart, self.products, "Laptop")
        expected = "Laptop has been added to your cart."
        self.assertIn("Laptop", self.cart)
        self.assertEqual(actual, expected)

    def test_add_to_cart_nonexistent_product(self):
        actual = jessicasStoreFunction.add_to_cart(self.cart, self.products, "Tablet")
        expected = "Product not found."
        self.assertNotIn("Tablet", self.cart)
        self.assertEqual(actual, expected)

    def test_view_cart_with_items(self):
        self.cart.append("Laptop")
        actual = jessicasStoreFunction.view_cart(self.cart, self.products)
        expected = "Laptop - $1000"
        self.assertEqual(actual, expected)

    def test_view_cart_empty(self):
        actual = jessicasStoreFunction.view_cart(self.cart, self.products)
        expected = None
        self.assertEqual(actual, expected)

    def test_remove_from_cart_existing_item(self):
        self.cart.append("Laptop")
        actual = jessicasStoreFunction.remove_from_cart(self.cart, "Laptop")
        expected = "Laptop has been removed from your cart."
        self.assertNotIn("Laptop", self.cart)
        self.assertEqual(actual, expected)

    def test_remove_from_cart_nonexistent_item(self):
        actual = jessicasStoreFunction.remove_from_cart(self.cart, "Tablet")
        expected = "Item not found in cart."
        self.assertEqual(actual, expected)

    def test_calculate_total(self):
        self.cart.extend(["Laptop", "Phone", "Headphones"])
        actual = jessicasStoreFunction.calculate_total(self.cart, self.products)
        expected = 1600
        self.assertEqual(actual, expected)

    def test_checkout(self):
        self.cart.extend(["Laptop", "Phone"])
        actual = jessicasStoreFunction.checkout(self.cart, self.products)
        expected = "Thank you for shopping with us! Your total is $1500."
        self.assertEqual(actual, expected)
        self.assertEqual(len(self.cart), 2)

