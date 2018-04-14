# FahrenheitToCelsius Exception Handling Tests
A Python Exception Handling UnitTest Challenge

**Goal:**
----------
You will write a math function titled, `fahrenheitToCelsius()` that receives a floating point number (fahrenheit) calculates celsius and returns a floating point number (celsius). In addition, it should not crash if incorrect information is passed to it.

**Notes:**
----------

* `fahrenheitToCelsius()` receives 1 input: an integer, float, or string (fahrenheit)
* `fahrenheitToCelsius()` will try to convert the input to a float and if it is unable to convert a string to a float, it will return -9999 to indicate there was an error
* `fahrenheitToCelsius()` converts temperatures in degrees Fahrenheit to Celsius by subtracting 32 and multiply by .5556 (or 5/9).
  * Example: `(50°F - 32) x .5556 = 10°C`
* `fahrenheitToCelsius()` needs to round celsius to the nearest tenth
  * `-15.001199999999999` will be rounded to `-15.0`
  * `100.008` will be rounded to `100.0`
* `fahrenheitToCelsius()` needs to incorporate Exception Handling in addition to performing the expected function

**Examples:**
inputs => output/s
--------------------------------
* "ten" => -9999
* 212 => 100.0
* 32 => 0.0
* 5 => -15.0
