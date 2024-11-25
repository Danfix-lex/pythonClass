from unittest import TestCase
import highestAndLowestScoresFunction

class TestHighestAndLowestScoreFunction(TestCase):
    def test_if_function_exist(self):
        student_names = [
    "Hamid", "Edwin", "Samuel", "Ifeayin", "Divine", 
    "Oyinyechi", "Emmanuel", "Christopher", "Ogene", "Dozie"
]
        subjects = ["C#", "Python", "Java", "Java Script"]
        marks = [
            [90, 85, 88, 92],  
            [78, 82, 91, 86],  
            [85, 95, 87, 88],  
            [92, 80, 85, 89],  
            [84, 89, 94, 90],  
            [75, 88, 80, 85],  
            [92, 76, 93, 87],  
            [89, 81, 86, 83],  
            [80, 77, 91, 93],  
            [84, 88, 79, 91]   
        ]
        
        expected_highest = ['Ifeayin', 'Bobo', 'Dayo', 'Ogene']  
        expected_lowest = ['Tunde', 'Chichi', 'Bayo', 'Ifeayin']  
        highest, lowest = highestAndLowestScoresFunction.get_highest_and_lowest_students_scores(students_data, subjects)
        
        self.assertEqual(highest, expected_highest)
        self.assertEqual(lowest, expected_lowest)

