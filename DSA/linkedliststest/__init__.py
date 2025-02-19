import unittest
from linkedlists import LinkedList

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.ll = LinkedList()

    def test_append(self):
        self.ll.append(10)
        self.ll.append(20)
        self.assertEqual(self.ll.size(), 2)
        self.assertEqual(self.ll.head.data, 10)
        self.assertEqual(self.ll.head.next.data, 20)

    def test_prepend(self):
        self.ll.prepend(10)
        self.ll.prepend(5)
        self.assertEqual(self.ll.size(), 2)
        self.assertEqual(self.ll.head.data, 5)
        self.assertEqual(self.ll.head.next.data, 10)

    def test_delete(self):
        self.ll.append(10)
        self.ll.append(20)
        self.ll.append(30)
        self.ll.delete(20)
        self.assertEqual(self.ll.size(), 2)
        self.assertEqual(self.ll.head.data, 10)
        self.assertEqual(self.ll.head.next.data, 30)

    def test_delete_head(self):
        self.ll.append(10)
        self.ll.append(20)
        self.ll.delete(10)
        self.assertEqual(self.ll.size(), 1)
        self.assertEqual(self.ll.head.data, 20)

    def test_delete_non_existent(self):
        self.ll.append(10)
        self.ll.append(20)
        result = self.ll.delete(30)
        self.assertEqual(result, "Data not found in the linked list")
        self.assertEqual(self.ll.size(), 2)

    def test_search(self):
        self.ll.append(10)
        self.ll.append(20)
        self.assertTrue(self.ll.search(10))
        self.assertTrue(self.ll.search(20))
        self.assertFalse(self.ll.search(30))

    def test_size(self):
        self.assertEqual(self.ll.size(), 0)
        self.ll.append(10)
        self.assertEqual(self.ll.size(), 1)
        self.ll.append(20)
        self.assertEqual(self.ll.size(), 2)

    def test_is_empty(self):
        self.assertTrue(self.ll.is_empty())
        self.ll.append(10)
        self.assertFalse(self.ll.is_empty())

    def test_display(self):
        self.ll.append(10)
        self.ll.append(20)
        self.ll.append(30)
        import io
        from contextlib import redirect_stdout
        f = io.StringIO()
        with redirect_stdout(f):
            self.ll.display()
        output = f.getvalue().strip()
        self.assertEqual(output, "10 -> 20 -> 30 -> None")

if __name__ == "__main__":
    unittest.main()