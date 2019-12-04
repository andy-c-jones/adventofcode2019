from day4.password import find_password_in_range, find_password_in_range_part2
import unittest

class TestPasswordPuzzle(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(find_password_in_range(356261, 846303), 544)

    def test_part2(self):
        self.assertEqual(find_password_in_range_part2(356261, 846303), 334)

