from order import Order

class Customer:
    all_customers = []

    def __init__(self, name):
        self.name = name
        Customer.all_customers.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise ValueError("Name must be a string between 1 and 15 characters.")

    def orders(self):
        return [order for order in Order.all() if order.customer == self]

    def coffees(self):
        return list(set(order.coffee for order in self.orders()))

    def create_order(self, coffee, price):
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        customer_totals = {}

        for order in Order.all():
            if order.coffee == coffee:
                if order.customer not in customer_totals:
                    customer_totals[order.customer] = 0
                customer_totals[order.customer] += order.price

        if not customer_totals:
            return None

        return max(customer_totals, key=customer_totals.get)
