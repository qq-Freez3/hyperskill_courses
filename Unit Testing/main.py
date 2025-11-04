import unittest

def simple_example_test():
    add = lambda x, y: x + y #function to be tested

    x = y = 2
    expected_result = 4 #expected result from add method

    output = add(x, y) #add method being tested
    print("Pass") if expected_result == output else print("Fail")

def quadratic_function():
    quadratic = lambda x: x**2 + 2*x + 1

    x = 5
    expected_result = 36 #do the math yourself to find expected result

    output = quadratic(x)
    print("Pass") if expected_result == output else print("Fail")
    if expected_result == output: print(f'Quadratic(2) is {quadratic(2)}')

# Functions to test
def add(x, y):
    return x + y
def power(x, y):
    return x ** y

# Unit Test
class TestMathOps(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(8, 9), 17) # test if 8 + 9 = 17
    def test_power(self):
        self.assertEqual(power(5, 2), 25) # test if 5^2 = 25
        self.assertEqual(power(2, 0), 1) # edge case

if __name__ == "__main__":
    #simple_example_test()
    #quadratic_function()
    unittest.main()