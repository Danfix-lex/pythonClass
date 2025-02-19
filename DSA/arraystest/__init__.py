import unittest
from arrays import Array

class TestArray(unittest.TestCase):
    def setUp(self):
        self.arr = Array()

    def test_insert_and_size(self):
        self.arr.insert(10)
        self.arr.insert(20)
        self.arr.insert(30)
        self.assertEqual(self.arr.size(), 3)

    def test_remove_at(self):
        self.arr.insert(10)
        self.arr.insert(20)
        self.arr.insert(30)
        removed_item = self.arr.remove_at(1)
        self.assertEqual(removed_item, 20)
        self.assertEqual(self.arr.size(), 2)

    def test_remove_at_invalid_index(self):
        self.arr.insert(10)
        self.assertEqual(self.arr.remove_at(5), "Index out of bounds")
        self.assertEqual(self.arr.remove_at(-1), "Index out of bounds")

    def test_get(self):
        self.arr.insert(10)
        self.arr.insert(20)
        self.assertEqual(self.arr.get(0), 10)
        self.assertEqual(self.arr.get(1), 20)

    def test_get_invalid_index(self):
        self.arr.insert(10)
        self.assertEqual(self.arr.get(5), "Index out of bounds")
        self.assertEqual(self.arr.get(-1), "Index out of bounds")

    def test_index_of(self):
        self.arr.insert(10)
        self.arr.insert(20)
        self.arr.insert(30)
        self.assertEqual(self.arr.index_of(20), 1)
        self.assertEqual(self.arr.index_of(40), -1)

    def test_is_empty(self):
        self.assertTrue(self.arr.is_empty())
        self.arr.insert(10)
        self.assertFalse(self.arr.is_empty())

    def test_print_array(self):
        self.arr.insert(10)
        self.arr.insert(20)
        self.arr.insert(30)
        self.arr.print_array()  # This will print to the console, so manually verify output

if __name__ == "__main__":
    unittest.main()