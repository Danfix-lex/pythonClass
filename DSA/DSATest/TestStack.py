import unittest

class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()
    
    def test_empty_stack(self):
        self.assertTrue(self.stack.is_empty())
        self.assertEqual(self.stack.size(), 0)
        self.assertEqual(self.stack.pop(), "Stack is empty")
        self.assertEqual(self.stack.peek(), "Stack is empty")
    
    def test_push(self):
        self.stack.push(1)
        self.assertFalse(self.stack.is_empty())
        self.assertEqual(self.stack.size(), 1)
        self.assertEqual(self.stack.peek(), 1)
        
        self.stack.push(2)
        self.assertEqual(self.stack.size(), 2)
        self.assertEqual(self.stack.peek(), 2)
    
    def test_pop(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        
        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(self.stack.size(), 2)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.size(), 1)
        self.assertEqual(self.stack.pop(), 1)
        self.assertTrue(self.stack.is_empty())
    
    def test_peek(self):
        self.stack.push("test")
        self.assertEqual(self.stack.peek(), "test")
        self.assertEqual(self.stack.size(), 1)
        
        self.stack.push("test2")
        self.assertEqual(self.stack.peek(), "test2")
        self.assertEqual(self.stack.size(), 2)
    
    def test_multiple_operations(self):
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.pop(), 2)
        self.stack.push(3)
        self.assertEqual(self.stack.peek(), 3)
        self.assertEqual(self.stack.size(), 2)

if __name__ == '__main__':
    unittest.main()
