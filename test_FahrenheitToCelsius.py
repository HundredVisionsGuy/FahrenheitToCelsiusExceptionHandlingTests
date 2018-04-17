# test_MathFunctions.py
# Tests Temp Converter functions

import unittest
from FahrenheitToCelsius import fahrenheitToCelsius
import re

class KnownValues(unittest.TestCase):
    # Set up
    def setUp(self):
        # get text from script for regex tests
        self.textfile = open('FahrenheitToCelsius.py', 'r')
        self.scripttext = self.textfile.read()
    # Tear down
    def tearDown(self):
        # close the file
        self.textfile.close()
    # Test regex search for a pattern in script
    def test_try_cmd_present(self):
        matches = re.findall("try:", self.scripttext)
        match = matches[0]
        self.assertEquals("try:", match)
        
    def test_except_block_present(self):
        matches = re.findall("except ValueError:", self.scripttext)
        matches += re.findall("except:", self.scripttext)
        hasMatch = bool(matches)
        self.assertEquals(True, hasMatch)

    def test_fahrenheitToCelsius_forTypeError(self):
        # Capture the results of the function
        result = fahrenheitToCelsius("str")
        # Check for expected output
        self.assertEqual(-9999, result)
    def test_fahrenheitToCelsius_forTypeErrorReturn(self):
        # Capture the results of the function
        #result = fahrenheitToCelsius("str")
        # Check for expected output
        self.assertRaises(TypeError, fahrenheitToCelsius("str"))

    # For expected results (no exceptions...get it?)
    def test_fahrenheitToCelsius_for212F(self):
        # Capture the results of the function
        result = fahrenheitToCelsius(212)
        # Check for expected output
        self.assertEqual(100.0, result)

    def test_fahrenheitToCelsius_for32F(self):
        # Capture the results of the function
        result = fahrenheitToCelsius(32)
        # Check for expected output
        self.assertEqual(0.0, result)

    def test_fahrenheitToCelsius_for5F(self):
        # Capture the results of the function
        result = fahrenheitToCelsius(5)
        # Check for expected output
        self.assertEqual(-15.0, result)
    
    def test_fahrenheitToCelsius_for50F(self):
        # Capture the results of the function
        result = fahrenheitToCelsius(50)
        # Check for expected output
        self.assertEqual(10.0, result)


# Run the tests
if __name__ == '__main__':
    unittest.main()
