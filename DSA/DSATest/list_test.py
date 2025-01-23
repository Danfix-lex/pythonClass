import unittest
from DSA.list_function import list_function

class TestListFunction(unittest.TestCase):
    def test_is_empty(self):
        list_func = list_function()
        self.assertTrue(list_func.is_empty())

    def test_size(self):
        list_func = list_function()
        self.assertEqual(0, list_func.size())

    def test_is_not_empty(self):
        list_func = list_function()
        list_func.add("Hello")
        self.assertTrue(list_func.is_not_empty())

    def test_element_add(self):
        list_func = list_function()
        list_func.add("Hello")
        self.assertEqual(1, list_func.size())

    def test_element_remove(self):
        list_func = list_function()
        list_func.add("Hello")
        list_func.remove("Hello")
        self.assertEqual(0, list_func.size())

    def test_multiple_element_add(self):
        list_func = list_function()
        list_func.add("Hello")
        list_func.add("World")
        list_func.add("MY")
        list_func.add("Name")
        list_func.add("Is")
        list_func.add("Danfix")
        self.assertEqual(6, list_func.size())

    def test_multiple_element_remove(self):
        list_func = list_function()
        list_func.add("Hello")
        list_func.add("World")
        list_func.add("MY")
        list_func.add("Name")
        list_func.add("Is")
        list_func.add("Danfix")
        list_func.remove("Danfix")
        list_func.remove("World")
        list_func.remove("MY")
        list_func.remove("Name")
        self.assertEqual(2, list_func.size())

    def test_index_of_list(self):
        list_func = list_function()
        list_func.add("Hello")
        list_func.add("World")
        list_func.add("MY")
        list_func.add("Name")
        list_func.add("Is")
        list_func.add("Danfix")
        self.assertEqual(3, list_func.index("Name"))

    def test_remove_index_of_list(self):
        list_func = list_function()
        list_func.add("Hello")
        list_func.add("World")
        list_func.add("MY")
        list_func.add("Name")
        list_func.add("Is")
        list_func.add("Danfix")
        self.assertEqual(5, list_func.index("Danfix"))

if __name__ == '__main__':
    unittest.main()