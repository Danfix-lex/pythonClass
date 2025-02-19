import unittest
from queues import Queue

class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_enqueue(self):
        self.queue.enqueue(10)
        self.queue.enqueue(20)
        self.assertEqual(self.queue.size(), 2)
        self.assertEqual(self.queue.peek(), 10)

    def test_dequeue(self):
        self.queue.enqueue(10)
        self.queue.enqueue(20)
        self.assertEqual(self.queue.dequeue(), 10)
        self.assertEqual(self.queue.size(), 1)
        self.assertEqual(self.queue.dequeue(), 20)
        self.assertEqual(self.queue.size(), 0)
        self.assertEqual(self.queue.dequeue(), "Queue is empty")

    def test_peek(self):
        self.queue.enqueue(10)
        self.queue.enqueue(20)
        self.assertEqual(self.queue.peek(), 10)
        self.queue.dequeue()
        self.assertEqual(self.queue.peek(), 20)
        self.queue.dequeue()
        self.assertEqual(self.queue.peek(), "Queue is empty")

    def test_is_empty(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.enqueue(10)
        self.assertFalse(self.queue.is_empty())
        self.queue.dequeue()
        self.assertTrue(self.queue.is_empty())

    def test_size(self):
        self.assertEqual(self.queue.size(), 0)
        self.queue.enqueue(10)
        self.assertEqual(self.queue.size(), 1)
        self.queue.enqueue(20)
        self.assertEqual(self.queue.size(), 2)
        self.queue.dequeue()
        self.assertEqual(self.queue.size(), 1)
        self.queue.dequeue()
        self.assertEqual(self.queue.size(), 0)

if __name__ == "__main__":
    unittest.main()