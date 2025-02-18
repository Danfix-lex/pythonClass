import unittest

import Diaries
import Diary


class DiariesTest(unittest.TestCase):
    def test_can_add_and_find_diary(self):
        diaries = Diaries()

        diary1 = Diary("Sam", "passSam")
        diary2 = Diary("Divine", "passDivine")

        diaries.add_diary(diary1)
        diaries.add_diary(diary2)

        found_sam_diary = diaries.find_diary_by_username("Sam")
        found_divine_diary = diaries.find_diary_by_username("Divine")

        self.assertIsNotNone(found_sam_diary, "Diary for Sam should be found.")
        self.assertIsNotNone(found_divine_diary, "Diary for Divine should be found.")
        self.assertEqual("Sam", found_sam_diary.get_username())
        self.assertEqual("Divine", found_divine_diary.get_username())

    def test_finding_non_existent_diary_returns_none(self):
        diaries = Diaries()
        diary1 = Diary("Sam", "passSam")
        diaries.add_diary(diary1)

        self.assertIsNone(diaries.find_diary_by_username("Esther"),
                          "Should return None for a non-existent diary.")

    def test_can_delete_diary(self):
        diaries = Diaries()

        diary1 = Diary("Sam", "passSam")
        diary2 = Diary("Divine", "passDivine")
        diaries.add_diary(diary1)
        diaries.add_diary(diary2)

        diaries.delete_diary("Sam")

        self.assertIsNone(diaries.find_diary_by_username("Sam"),
                          "Sam's diary should be deleted.")
        self.assertIsNotNone(diaries.find_diary_by_username("Divine"),
                             "Divine's diary should still be present.")

if __name__ == '__main__':
    unittest.main()