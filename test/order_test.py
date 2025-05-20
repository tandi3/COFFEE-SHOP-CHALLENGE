import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestOrder(unittest.TestCase):
    def test_valid_order_creation(self):
        customer = Customer("Alice")
        coffee = Coffee("Latte")
        order = Order(customer, coffee, 4.0)
        self.assertEqual(order.customer, customer)
        self.assertEqual(order.coffee, coffee)
        self.assertEqual(order.price, 4.0)

    def test_invalid_order_price(self):
        customer = Customer("Bob")
        coffee = Coffee("Espresso")
        with self.assertRaises(ValueError):
            Order(customer, coffee, 15.0)

if __name__ == "__main__":
    unittest.main()
