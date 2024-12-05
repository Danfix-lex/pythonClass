from unittest import TestCase
import listCubeTotal

class TestPrimeInListFunction(TestCase):
    def test_if_function_is_correct(self):
        actual = listCubeTotal.get_list_cube_total([1,2,3,4,5])
        expected = [1,8,27,64,125]
        self.assertEqual(actual, expected)
