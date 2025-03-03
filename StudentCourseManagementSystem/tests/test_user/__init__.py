import unittest
from models.user import User

class TestUser(unittest.TestCase):
    def test_user_creation(self):
        user = User(1, "john_doe", "password123", "student")
        self.assertEqual(user.username, "john_doe")
        self.assertTrue(user.verify_password("password123"))

if __name__ == '__main__':
    unittest.main()