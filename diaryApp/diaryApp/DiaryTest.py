import unittest

import Diary


class DiaryTest(unittest.TestCase):
    def test_that_diary_can_be_created(self):
        name = "stephen"
        password = "password123"
        diary = (name, password)
        self.assertIsNotNone(diary)

    def test_that_diary_is_locked(self):
        name = "stephen"
        password = "password123"
        diary = Diary(name, password)
        self.assertTrue(diary.is_locked())

    def test_that_diary_can_be_unlocked_with_correct_password(self):
        name = "Bamsy"
        password = "password123"
        diary = Diary(name, password)
        diary.unlock_diary(password)
        self.assertFalse(diary.is_locked())

    def test_that_diary_can_be_locked(self):
        name = "Bamsy"
        password = "password123"
        diary = Diary(name, password)
        diary.unlock_diary(password)
        diary.lock_diary()
        self.assertTrue(diary.is_locked())

    def test_that_diary_cannot_create_entry_when_locked(self):
        name = "Bamsy"
        password = "password123"
        diary = Diary(name, password)

        with self.assertRaises(Exception):
            diary.create_entry("My Secret", "This is a private note")

    def test_that_diary_can_create_entry_when_unlocked(self):
        name = "Bamsy"
        password = "password123"
        diary = Diary(name, password)
        diary.unlock_diary(password)

        try:
            diary.create_entry("My Day", "It was amazing!")
        except Exception as e:
            self.fail("create_entry raised an exception unexpectedly: " + str(e))

    def test_that_diary_cannot_create_entry_with_empty_title_or_body(self):
        name = "Bamsy"
        password = "password123"
        diary = Diary(name, password)
        diary.unlock_diary(password)

        with self.assertRaises(ValueError):
            diary.create_entry("", "This is a test")
        with self.assertRaises(ValueError):
            diary.create_entry("Title", "")

    def test_that_we_can_find_entry_by_id(self):
        name = "Bamsy"
        password = "password123"
        diary = Diary(name, password)
        diary.unlock_diary(password)
        diary.create_entry("My First Entry", "This is my first diary entry.")
        diary.create_entry("Second Entry", "Another entry in my diary.")
        found_entry = diary.find_entry_by_id(1)
        self.assertIsNotNone(found_entry)
        self.assertEqual(found_entry.title, "My First Entry")

    def test_that_finding_non_existent_entry_returns_none(self):
        name = "Bamsy"
        password = "password123"
        diary = Diary(name, password)
        diary.unlock_diary(password)
        self.assertIsNone(diary.find_entry_by_id(99))

    def test_that_we_can_update_entry(self):
        name = "Bamsy"
        password = "password123"
        diary = Diary(name, password)
        diary.unlock_diary(password)
        diary.create_entry("Old Title", "Old Body")
        diary.update_entry(1, "New Title", "New Body")
        updated_entry = diary.find_entry_by_id(1)
        self.assertEqual(updated_entry.title, "New Title")
        self.assertEqual(updated_entry.body, "New Body")

    def test_that_updating_non_existent_entry_throws_exception(self):
        name = "Bamsy"
        password = "password123"
        diary = Diary(name, password)
        diary.unlock_diary(password)

        with self.assertRaises(ValueError):
            entry_id = 99
            diary.update_entry(entry_id, "New Title", "New Body")

    def test_that_we_can_delete_entry(self):
        name = "Bamsy"
        password = "password123"
        diary = Diary(name, password)
        diary.unlock_diary(password)
        diary.create_entry("Title", "Body")
        diary.delete_entry(1)
        self.assertIsNone(diary.find_entry_by_id(1))

    def test_that_deleting_non_existent_entry_does_nothing(self):
        name = "Bamsy"
        password = "password123"
        diary = Diary(name, password)
        diary.unlock_diary(password)

        try:
            diary.delete_entry(99)
        except Exception as e:
            self.fail("delete_entry raised an exception for a non-existent entry: " + str(e))

    def test_that_updating_entry_changes_time(self):
        name = "Bamsy"
        password = "password123"
        diary = Diary(name, password)
        diary.unlock_diary(password)
        diary.create_entry("Old Title", "Old Body")
        entry = diary.find_entry_by_id(1)

        original_time = getattr(entry, 'time', None)
        entry_id = 1
        diary.update_entry(entry_id, "New Title", "New Body")
        updated_entry = diary.find_entry_by_id(1)

        self.assertIs(updated_entry, entry)

        if original_time is not None:
            self.assertNotEqual(updated_entry.time, original_time)

if __name__ == '__main__':
    unittest.main()