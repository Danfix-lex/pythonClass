import unittest
from stacks import Stack

class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

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

    def test_stack_overflow(self):
        stack = Stack(2)
        stack.push(10)
        stack.push(20)
        with self.assertRaises(Exception):
            stack.push(30)

if __name__ == "__main__":
    unittest.main()