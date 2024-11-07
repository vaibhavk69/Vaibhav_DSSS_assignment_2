import unittest
import random
from math_quiz import getNumber, getOperation, caculate


class TestMathGame(unittest.TestCase):

    def test_getNumber(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = getNumber(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_getOperation(self):
        # Test if operations are performed from the specified criteria only
        test_cases = ['+', '-', '*']
        for _ in range(100): 
            operation = getOperation()
            self.assertTrue(operation in test_cases)
        # TODO

    def test_calculate(self):
            # test if the expected output is exactly same as the actual output
            test_cases = [(5, 2, '+', '5 + 2', 7), (7, 3, '-', '7 - 3', 4), (9, 5, '-', '9 - 5', 4), (6, 3, '+', '6 + 3', 9)]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                PROBLEM, ANSWER = caculate(num1, num2, operator)
                self.assertTrue(PROBLEM == expected_problem)
                self.assertTrue(ANSWER == expected_answer)     
                
                # TODO
                

if __name__ == "__main__":
    unittest.main()
