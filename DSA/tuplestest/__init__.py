import unittest
from tuples import TupleStack

class TestTupleStack(unittest.TestCase):
    def setUp(self):
        self.stack = TupleStack()

    def test_push_and_size(self):
        self.stack.push(10)
        self.stack.push(20)
        self.assertEqual(self.stack.size(), 2)

    def test_pop(self):
        self.stack.push(10)
        self.stack.push(20)
        self.assertEqual(self.stack.pop(), 20)
        self.assertEqual(self.stack.pop(), 10)
        self.assertEqual(self.stack.pop(), "Stack is empty")

    def test_peek(self):
        self.stack.push(10)
        self.stack.push(20)
        self.assertEqual(self.stack.peek(), 20)
        self.stack.pop()
        self.assertEqual(self.stack.peek(), 10)
        self.stack.pop()
        self.assertEqual(self.stack.peek(), "Stack is empty")

    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.push(10)
        self.assertFalse(self.stack.is_empty())
        self.stack.pop()
        self.assertTrue(self.stack.is_empty())

    def test_size(self):
        self.assertEqual(self.stack.size(), 0)
        self.stack.push(10)
        self.assertEqual(self.stack.size(), 1)
        self.stack.push(20)
        self.assertEqual(self.stack.size(), 2)
        self.stack.pop()
        self.assertEqual(self.stack.size(), 1)

if __name__ == "__main__":
    unittest.main()