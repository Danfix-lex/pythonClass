import unittest
from sets import Set

class SetTest(unittest.TestCase):
    def setUp(self):
        self.set1 = Set()
        self.set1.add(1)
        self.set1.add(2)
        self.set1.add(3)

        self.set2 = Set()
        self.set2.add(3)
        self.set2.add(4)
        self.set2.add(5)

    def test_add(self):
        self.set1.add(4)
        self.assertTrue(self.set1.contains(4))
        self.set1.add(2)
        self.assertEqual(self.set1.size(), 4)

    def test_remove(self):
        self.set1.remove(2)
        self.assertFalse(self.set1.contains(2))
        self.assertEqual(self.set1.size(), 2)
        with self.assertRaises(ValueError):
            self.set1.remove(10)  # Removing a non-existent element should raise an error

    def test_contains(self):
        self.assertTrue(self.set1.contains(1))
        self.assertFalse(self.set1.contains(10))

    def test_size(self):
        self.assertEqual(self.set1.size(), 3)
        self.set1.add(4)
        self.assertEqual(self.set1.size(), 4)

    def test_is_empty(self):
        empty_set = Set()
        self.assertTrue(empty_set.is_empty())
        self.assertFalse(self.set1.is_empty())

    def test_union(self):
        union_set = self.set1.union(self.set2)
        expected_elements = {1, 2, 3, 4, 5}
        for element in expected_elements:
            self.assertTrue(union_set.contains(element))
        self.assertEqual(union_set.size(), 5)

    def test_intersection(self):
        intersection_set = self.set1.intersection(self.set2)
        self.assertTrue(intersection_set.contains(3))
        self.assertEqual(intersection_set.size(), 1)

    def test_difference(self):
        difference_set = self.set1.difference(self.set2)
        self.assertTrue(difference_set.contains(1))
        self.assertTrue(difference_set.contains(2))
        self.assertFalse(difference_set.contains(3))
        self.assertEqual(difference_set.size(), 2)

    def test_str(self):
        self.assertEqual(str(self.set1), "{1, 2, 3}")
        self.assertEqual(str(self.set2), "{3, 4, 5}")

if __name__ == "__main__":
    unittest.main()