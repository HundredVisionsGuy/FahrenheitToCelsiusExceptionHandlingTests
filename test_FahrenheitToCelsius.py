# test_MathFunctions.py
# Tests Temp Converter functions

import unittest
import MathFunctions

class KnownValues(unittest.TestCase):
    
    ################################################
    # test divisibility
    ################################################
    # for exception handling
    def test_divisibility_forZeroDivisionErrorHandling(self):
        # Capture the results of the function
        self.assertEquals('error', MathFunctions.divisibility(10,0))
    def test_divisibility_forValueErrorHandling(self):
        self.assertEquals('error', MathFunctions.divisibility(10, 'five'))
    # for expected results
    def test_divisibility_forEvenlyDivisible(self):
        result = MathFunctions.divisibility(21, 3)
        self.assertEquals('divides evenly', result)
    def test_divisibility_forNotEvenlyDivisible(self):
        result = MathFunctions.divisibility(5,2)
        self.assertEquals("doesn't divide evenly", result)

    
    ################################################
    # test fahrenheitToCelsius
    ################################################
    # For exception Handling
    def test_fahrenheitToCelsius_forTypeError(self):
        # Capture the results of the function
        result = MathFunctions.fahrenheitToCelsius("str")
        # Check for expected output
        self.assertEqual(-9999, result)
    def test_fahrenheitToCelsius_forTypeErrorReturn(self):
        # Capture the results of the function
        #result = MathFunctions.fahrenheitToCelsius("str")
        # Check for expected output
        self.assertRaises(TypeError, MathFunctions.fahrenheitToCelsius("str"))

    # For expected results (no exceptions...get it?)
    def test_fahrenheitToCelsius_for212F(self):
        # Capture the results of the function
        result = MathFunctions.fahrenheitToCelsius(212)
        # Check for expected output
        self.assertEqual(100.0, result)

    def test_fahrenheitToCelsius_for32F(self):
        # Capture the results of the function
        result = MathFunctions.fahrenheitToCelsius(32)
        # Check for expected output
        self.assertEqual(0.0, result)

    def test_fahrenheitToCelsius_for5F(self):
        # Capture the results of the function
        result = MathFunctions.fahrenheitToCelsius(5)
        # Check for expected output
        self.assertEqual(-15.0, result)
    
    def test_fahrenheitToCelsius_for50F(self):
        # Capture the results of the function
        result = MathFunctions.fahrenheitToCelsius(50)
        # Check for expected output
        self.assertEqual(10.0, result)
        
    ################################################
    # Test celsiusToFahrenheit()
    ################################################
    # For exception Handling
    def test_celsiusToFahrenheit_forTypeError(self):
        # Capture the results of the function
        result = MathFunctions.celsiusToFahrenheit("str")
        # Check for expected output
        self.assertEqual(-9999, result)
    def test_celsiusToFahrenheit_forTypeErrorReturn(self):
        # Capture the results of the function
        #result = MathFunctions.fahrenheitToCelsius("str")
        # Check for expected output
        self.assertRaises(TypeError, MathFunctions.celsiusToFahrenheit("str"))

    # For expected output
    def test_celsiusToFahrenheit_for0C(self):
        # Capture the results of the function
        result = MathFunctions.celsiusToFahrenheit(0)
        # Check for expected output
        self.assertEqual(32.0, result)

    def test_celsiusToFahrenheit_for100C(self):
        # Capture the results of the function
        result = MathFunctions.celsiusToFahrenheit(100)
        # Check for expected output
        self.assertEqual(212.0, result)

    def test_celsiusToFahrenheit_for55C(self):
        # Capture the results of the function
        result = MathFunctions.celsiusToFahrenheit(55)
        # Check for expected output
        self.assertEqual(131.0, result)
        

    def test_celsiusToFahrenheit_forMinus50C(self):
        # Capture the results of the function
        result = MathFunctions.celsiusToFahrenheit(-50)
        # Check for expected output
        self.assertEqual(-58.0, result)

# Run the tests
if __name__ == '__main__':
    unittest.main()
