import unittest
import gradingProgramFunction

class TestSearchElement(unittest.TestCase):
    def test_grade_program_is_correct(self):
        actual = gradingProgramFunction.get_students_score_grade({"Gloria": 88, "Divine": 78, "Esther": 65, "Mercy": 75, "Uzo": 71})
        expected = {"Gloria": "Exceeds Expectations", "Divine": "Acceptable", "Esther": "Fail", "Mercy": "Acceptable", "Uzo": "Acceptable"}
        self.assertEqual(actual, expected)
if __name__ == "__main__":
    unittest.main()