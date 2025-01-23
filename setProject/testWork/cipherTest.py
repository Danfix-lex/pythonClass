import unittest
from classWork import cipher

class TestWork(unittest.TestCase):
    def test_if_encryption_is_correct(self):
        actual = cipher.get_cipher_encryption_key("Hello,World!")
        expected = "Uryyb,Jbeyq!"
        self.assertEqual(actual, expected)

    def test_if_encryption_is_not_correct(self):
        actual = cipher.get_cipher_encryption_key("Welcome To Python!")
        expected = "Jrypbzr Gb Clguba!"
        self.assertEqual(actual, expected)

    def test_if_user_enters_an_integer(self):
        self.assertRaises(TypeError, cipher.get_cipher_encryption_key, 12345 )

    def test_if_user_enters_a_string_and_an_integer(self):
        self.assertRaises(TypeError, cipher.get_cipher_encryption_key, "Daniel", 12345)

    def test_if_user_enters_a_string_and_an_integer_together(self):
        actual = cipher.get_cipher_encryption_key("Daniel Ojo 12345")
        expected = "Qnavry Bwb 12345"
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()