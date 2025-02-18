import unittest
from diaryApp import Diary, Entry

class TestDiary(unittest.TestCase):
    def setUp(self):
        self.diary = Diary("testUser", "password123")

    def test_get_username(self):
        self.assertEqual(self.diary.get_username(), "testUser")

    def test_get_password(self):
        self.assertEqual(self.diary.get_password(), "password123")

    def test_lock_diary(self):
        self.diary.lock_diary()
        self.assertTrue(self.diary.is_diary_locked())

    def test_unlock_diary_with_correct_password(self):
        self.diary.lock_diary()
        self.diary.unlock_diary("password123")
        self.assertFalse(self.diary.is_diary_locked())

    def test_unlock_diary_with_wrong_password(self):
        self.diary.lock_diary()
        with self.assertRaises(ValueError):
            self.diary.unlock_diary("wrongPassword")

    def test_create_entry_when_unlocked(self):
        self.diary.create_entry("My Title", "My Entry Body")
        self.assertEqual(len(self.diary.get_entries()), 1)

    def test_create_entry_when_locked(self):
        self.diary.lock_diary()
        with self.assertRaises(RuntimeError):
            self.diary.create_entry("Locked Entry", "Cannot add this")

    def test_find_entry_by_id(self):
        self.diary.create_entry("Test Entry", "Test Body")
        entry = self.diary.find_entry_by_id(1)
        self.assertIsNotNone(entry)
        self.assertEqual(entry.get_title(), "Test Entry")

    def test_update_entry(self):
        self.diary.create_entry("Old Title", "Old Body")
        self.diary.update_entry(1, "New Title", "New Body")
        entry = self.diary.find_entry_by_id(1)
        self.assertEqual(entry.get_title(), "New Title")
        self.assertEqual(entry.get_body(), "New Body")

    def test_delete_entry(self):
        self.diary.create_entry("To be deleted", "Delete me")
        self.diary.delete_entry(1)
        self.assertIsNone(self.diary.find_entry_by_id(1))

if __name__ == '__main__':
    unittest.main()
