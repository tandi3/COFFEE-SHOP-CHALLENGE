import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer(unittest.TestCase):
    def test_customer_name_validation(self):
        with self.assertRaises(ValueError):
            Customer("")
        with self.assertRaises(ValueError):
            Customer("A name way too long")

    def test_customer_create_order(self):
        customer = Customer("Alice")
        coffee = Coffee("Latte")
        order = customer.create_order(coffee, 3.5)
        self.assertIn(order, Order.all())

if __name__ == "__main__":
    unittest.main()
