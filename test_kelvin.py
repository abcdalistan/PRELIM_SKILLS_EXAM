from temp_test import Temperature

import unittest

class test_kelvin(unittest.TestCase):
    def test_celsius(self):
        self.assertEqual(Temperature(celsius=35).kelvin, 308.15)

    def test_fahrenheit(self):
        self.assertEqual(Temperature(fahrenheit=12).kelvin, 262.038888889)

    def test_kelvin(self):
        self.assertEqual(Temperature(kelvin=27).kelvin, 27)

    def test_negative(self):
        self.assertEqual(Temperature(kelvin=-2),kelvin = -2)
    
if __name__ == '__main__':
    unittest.main()
