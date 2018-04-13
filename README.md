# MathFunctions.py
A Python 1 Exception Handling UnitTest Challenge

**Goal:**
----------
You will write 1 or more math functions that are designed to not only solve some math problems but also handle incorrect inputs (ZeroDivisionErrors, TypeErrors, ValueErrors)

**Inputs:**
----------
* `divisibilty()` receives 2 inputs: (numerator & denominator) and returns one of the following outputs:
 * "divides evenly" - if the numbers divide evenly (like `4 / 2`))
 * "doesn't divide evenly" - if the numerator is not evenly divisible by the denominator (like `5 / 2`)
 * "error" - if the inputs cannot be converted to integers (or floats) OR the denominator is `0` (since you cannot divide by 0)
 * **NOTE**: divisibility() should be able to accept strings provided they can be converted to a number (e.g. `divisibility('10', '3')`)
* `fahrenheitToCelsius()` receives 1 input: an integer, float, or string (fahrenheit)
* `fahrenheitToCelsius()` will try to convert the input to a float and *if it is unable to convert a string to a float, it will return -9999 to indicate there was an error*
* `fahrenheitToCelsius()` calculates area using the following formula: `area * 0.000207`
* `celsiusToFahrenheit()` receives 1 input: an integer, float, or string (celsius)
* `celsiusToFahrenheit()` will try to convert the input to a float and *if it is unable to convert a string to a float, it will return -9999 to indicate there was an error*
* `celsiusToFahrenheit()` calculates area using the following formula: `area * 247.10538`

**Notes/Challenge Opportunity**
-------------
* Each function needs to check to make sure the inputs can be converted to a number
* Each function needs to handle incorrect input (e.g. strings that can't be converted to numbers, a denominator that is 0)
* Each function will need to incorporate Exception Handling in addition to performing the expected function

**Examples:**
inputs => output/s
--------------------------------
* divisibilty:
  * 10 2 => "divides evenly"
  * 7 2 => "doesn't divide evenly"
  * 20 0 => "error"
  * "five" / "two" => "error"
* fahrenheitToCelsius:
  * "ten" => -9999
  * 212 => 100.0
  * 32 => 0.0
  * 5 => -15.0
* celsiusToFahrenheit:
  * "twenty" => -9999
  * 0 => 32.0
  * 100 => 212.0
  * 55 => 131.0
