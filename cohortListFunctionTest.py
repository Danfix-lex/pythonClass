import unittest
import cohortListFunction

class TestSearchElement(unittest.TestCase):
    def test_grade_program_is_correct(self):
        actual = cohortListFunction.get_cohort_and_months(["cohort24", "cohort23", "cohort22", "cohort21", "cohort20"], ["4months", "5months", "6months", "7months", "8months"])
        expected = {"cohort24":"4months", "cohort23":"5months", "cohort22":"6months", "cohort21":"7months", "cohort20":"8months"}
        self.assertEqual(actual, expected)
if __name__ == "__main__":
    unittest.main()

    # for subject, score in student["scores"].items():
    #     print(f"{subject}: {score}")