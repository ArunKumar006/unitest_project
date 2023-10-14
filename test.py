import unittest
from project.calc import sum

class TestCalculations(unittest.TestCase):

    def test_sum(self):
        calculation = sum(8, 2)
        self.assertEqual(calculation, 10, 'The sum is wrong.')

if __name__ == '__main__':
    unittest.main()
