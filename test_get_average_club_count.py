"""A3. Test cases for function club_functions.get_average_club_count.
"""

import unittest
import club_functions


class TestGetAverageClubCount(unittest.TestCase):
    """Test cases for function club_functions.get_average_club_count.
    """

    def test_00_empty(self):
        param = {}
        actual = club_functions.get_average_club_count(param)
        expected = 0.0
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertAlmostEqual(actual, expected, msg)

    def test_01_one_person_one_club(self):
        param = {'Claire Dunphy': ['Parent Teacher Association']}
        actual = club_functions.get_average_club_count(param)
        expected = 1.0
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertAlmostEqual(actual, expected, msg)

    def test_02_one_person_no_club(self):
        param = {'Claire Dunphy': []}
        actual = club_functions.get_average_club_count(param)
        expected = 0.0
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertAlmostEqual(actual, expected, msg)

    def test_03_one_person_two_club(self):
        param = {'Claire Dunphy': ['Parent Teacher Association', 'Chess Club']}
        actual = club_functions.get_average_club_count(param)
        expected = 2.0
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertAlmostEqual(actual, expected, msg)

    def test_04_two_people_one_club(self):
        param = {'Claire Dunphy': ['Parent Teacher Association'], 'Luke Dunphy': ['Chess Club']}
        actual = club_functions.get_average_club_count(param)
        expected = 1.0
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertAlmostEqual(actual, expected, msg)

    def test_05_two_people_two_clubs(self):
        param = {'Claire Dunphy': ['Parent Teacher Association', 'Mean Moms Club'
                                   ], 'Luke Dunphy': ['Chess Club', 'Student Council']}
        actual = club_functions.get_average_club_count(param)
        expected = 2.0
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertAlmostEqual(actual, expected, msg)

    def test_06_two_people_different_club_lengths(self):
        param = {'Claire Dunphy': ['Parent Teacher Association'
                                   ], 'Luke Dunphy': ['Chess Club', 'Student Council']}
        actual = club_functions.get_average_club_count(param)
        expected = 1.5
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertAlmostEqual(actual, expected, msg)    


if __name__ == '__main__':
    unittest.main(exit=False)
