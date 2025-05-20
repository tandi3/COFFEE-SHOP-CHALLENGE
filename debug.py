from customer import Customer
from coffee import Coffee
from order import Order


alice = Customer("Alice")
bob = Customer("Bob")
carol = Customer("Carol")


latte = Coffee("Latte")
espresso = Coffee("Espresso")
cappuccino = Coffee("Cappuccino")


order1 = Order(alice, latte, 4.5)
order2 = Order(bob, espresso, 3.0)
order3 = Order(alice, espresso, 3.5)
order4 = Order(carol, cappuccino, 5.0)
order5 = Order(bob, cappuccino, 4.8)
order6 = Order(alice, cappuccino, 4.9)


print(f"Alice's Orders: {alice.orders()}")
print(f"Alice's Coffees: {[coffee.name for coffee in alice.coffees()]}")


print(f"Cappuccino Orders: {cappuccino.orders()}")
print(f"Cappuccino Customers: {[customer.name for customer in cappuccino.customers()]}")


print(f"Number of Cappuccino Orders: {cappuccino.num_orders()}")
print(f"Average Price of Cappuccino: {cappuccino.average_price()}")


alice.create_order(latte, 4.7)
print(f"New Alice Orders: {alice.orders()}")


top_customer_for_cappuccino = Customer.most_aficionado(cappuccino)
if top_customer_for_cappuccino:
    print(f"Top spender on Cappuccino: {top_customer_for_cappuccino.name}")
else:
    print("No orders for Cappuccino yet.")


print("✅ Debug session complete.")
