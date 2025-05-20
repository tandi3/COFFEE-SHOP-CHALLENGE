import unittest
from coffee import Coffee

class TestCoffee(unittest.TestCase):
    def test_coffee_name_validation(self):
        with self.assertRaises(ValueError):
            Coffee("A")

    def test_coffee_name_immutable(self):
        coffee = Coffee("Latte")
        with self.assertRaises(AttributeError):
            coffee.name = "Mocha"

if __name__ == "__main__":
    unittest.main()
