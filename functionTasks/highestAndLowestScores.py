def find_highest_and_lowest(students, subjects, marks):
    highest_students = []
    lowest_students = []

    for subject_index in range(len(subjects)):
        highest_index = -1
        lowest_index = -1
        for student_index in range(len(students)):
            if highest_index == -1 or marks[student_index][subject_index] > marks[highest_index][subject_index]:
                highest_index = student_index
            if lowest_index == -1 or marks[student_index][subject_index] < marks[lowest_index][subject_index]:
                lowest_index = student_index
        
        highest_students.append(students[highest_index])
        lowest_students.append(students[lowest_index])

    return highest_students, lowest_students


# Now, let's set up the unit tests for this function
import unittest

class TestFindHighestAndLowest(unittest.TestCase):

    def test_highest_and_lowest(self):
        students = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah", "Ivy", "Jack"]
        subjects = ["Math", "English", "Science", "History"]
        marks = [
            [90, 85, 88, 92],  # Alice's marks
            [78, 82, 91, 86],  # Bob's marks
            [85, 95, 87, 88],  # Charlie's marks
            [92, 80, 85, 89],  # David's marks
            [84, 89, 94, 90],  # Eva's marks
            [75, 88, 80, 85],  # Frank's marks
            [92, 76, 93, 87],  # Grace's marks
            [89, 81, 86, 83],  # Hannah's marks
            [80, 77, 91, 93],  # Ivy's marks
            [84, 88, 79, 91]   # Jack's marks
        ]

        expected_highest = ['David', 'Charlie', 'Eva', 'Jack']
        expected_lowest = ['Frank', 'Grace', 'Frank', 'Hannah']
        
        highest, lowest = find_highest_and_lowest(students, subjects, marks)
        
        self.assertEqual(highest, expected_highest)
        self.assertEqual(lowest, expected_lowest)


if __name__ == '__main__':
    unittest.main()

