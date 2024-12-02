from unittest import TestCase
import pizzaApp

class TestPizzaOrder(TestCase):
    def test_calculate_order(self):
        result = pizzaApp.calculate_order(20, "Small Money")
        expected = {"boxes": 4, "leftover": 4, "price": 11600}
        self.assertEqual(result, expected)

