"""A3. Test cases for function club_functions.get_last_to_first.
"""

import unittest
import club_functions


class TestGetLastToFirst(unittest.TestCase):
    """Test cases for function club_functions.get_last_to_first.
    """

    def test_00_empty(self):
        param = {}
        actual = club_functions.get_last_to_first(param)
        expected = {}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)

    def test_01_one_person_one_friend_same_last(self):
        param = {'Clare Dunphy': ['Phil Dunphy']}
        actual = club_functions.get_last_to_first(param)
        expected = {'Dunphy': ['Clare', 'Phil']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)

    def test_02_one_person_one_friend_different_last(self):
        param = {'Clare Dunphy': ['Manny Delgado']}
        actual = club_functions.get_last_to_first(param)
        expected = {'Dunphy': ['Clare'], 'Delgado': ['Manny']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)

    def test_03_one_person_different_friends_same_last(self):
        param = {'Alex Dunphy': ['Luke Dunphy', 'Hailey Dunphy']}
        actual = club_functions.get_last_to_first(param)
        expected = {'Dunphy': ['Alex', 'Hailey', 'Luke']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)

    def test_04_one_person_different_friends_different_last(self):
        param = {'Clare Dunphy': ['Jay Pritchette', 'Manny Delgado']}
        actual = club_functions.get_last_to_first(param)
        expected = {'Dunphy': ['Clare'], 'Pritchette': ['Jay'], 'Delgado': ['Manny']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)

    def test_05_one_person_different_friends_some_same_last(self):
        param = {'Clare Dunphy': ['Hailey Dunphy', 'Andy Bailey']}
        actual = club_functions.get_last_to_first(param)
        expected = {'Dunphy': ['Clare', 'Hailey'], 'Bailey': ['Andy']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)

    def test_06_multi_people_one_friend_all_same_last(self):
        param = {'Clare Dunphy': ['Phil Dunphy'], 'Alex Dunphy': ['Luke Dunphy']}
        actual = club_functions.get_last_to_first(param)
        expected = {'Dunphy': ['Alex', 'Clare', 'Luke', 'Phil']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)

    def test_07_multi_people_one_friend_same_last(self):
        param = {'Clare Dunphy': ['Phil Dunphy'], 'Jay Pritchette': ['Joe Pritchette']}
        actual = club_functions.get_last_to_first(param)
        expected = {'Dunphy': ['Clare', 'Phil'], 'Pritchette': ['Jay', 'Joe']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)

    def test_08_multi_people_different_friends_same_last(self):
        param = {'Clare Dunphy': ['Phil Dunphy'], 'Alex Dunphy': ['Luke Dunphy', 'Hailey Dunphy']}
        actual = club_functions.get_last_to_first(param)
        expected = {'Dunphy': ['Alex', 'Clare', 'Hailey', 'Luke', 'Phil']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)

    def test_09_multi_people_one_friend_different_last(self):
        param = {'Clare Dunphy': ['Cameron Tucker'], 'Jay Pritchette': ['Manny Delgado']}
        actual = club_functions.get_last_to_first(param)
        expected = {'Dunphy': ['Clare'], 'Pritchette': ['Jay'], 'Delgado': ['Manny'], 'Tucker': ['Cameron']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)

    def test_10_multi_people_different_friends_different_last(self):
        param = {'Clare Dunphy': ['Cameron Tucker', 'Andy Bailey'], 'Jay Pritchette': ['Manny Delgado']}
        actual = club_functions.get_last_to_first(param)
        expected = {'Dunphy': ['Clare'], 'Pritchette': ['Jay'], 'Delgado': ['Manny'], 'Tucker': ['Cameron'], 'Bailey': ['Andy']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)

    def test_12_multi_people_different_friends_some_same_last(self):
        param = {'Clare Dunphy': ['Hailey Dunphy', 'Andy Bailey'], 'Jay Pritchette': ['Manny Delgado'],}
        actual = club_functions.get_last_to_first(param)
        expected = {'Dunphy': ['Clare', 'Hailey'], 'Pritchette': ['Jay'], 'Delgado': ['Manny'], 'Bailey': ['Andy']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)


if __name__ == '__main__':
    unittest.main(exit=False)
