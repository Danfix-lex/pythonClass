import unittest
from DSA.set_function import set_function

class TestListFunction(unittest.TestCase):
    def test_is_empty(self):
        set_func = set_function()
        self.assertTrue(set_func.is_empty())

    def test_size(self):
        set_func = set_function()
        self.assertEqual(0, set_func.size())

    def test_set_add_elements(self):
        set_func = set()
        set_func.add("Danfix")
        set_func.add("Fame")
        assert len(set_func) == 2

    def test_set_remove_elements(self):
        set_func = set()
        set_func.add("Danfix")
        set_func.add("Fame")
        set_func.remove("Fame")
        assert len(set_func) == 1

    def test_set_remove_elements_empty(self):
        set_func = set()
        set_func.add("Danfix")
        set_func.add("Fame")
        set_func.clear()
        assert len(set_func) == 0

if __name__ == '__main__':
    unittest.main()
