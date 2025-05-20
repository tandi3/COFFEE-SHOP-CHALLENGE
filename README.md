# COFFEE-SHOP-CHALLENGE

A simple Python OOP project modeling a coffee shop ordering system with customers, coffees, and orders.  
Built using classes, object relationships, properties, and class methods.


## 📖 Models & Relationships

### Customer
- Has a `name` (1-15 characters).
- Can place orders.
- Can retrieve their orders and the unique coffees they've ordered.
- Can check which customer is the **most aficionado** for a coffee (bonus method).

### Coffee
- Has a `name` (min 3 characters).
- Knows its orders and customers.
- Can report total number of orders.
- Can compute the average price of its orders.

### Order
- Belongs to a **Customer** and a **Coffee**.
- Has a `price` (float between 1.0–10.0).
- Immutable after creation.



## ✅ Features

- Class attributes for tracking all instances.
- Data validation for all attributes and properties.
- Clean object relationships connecting models.
- Aggregated data methods (like average price and number of orders).
- Class method to find the top spender on a specific coffee.
- Test suite covering the models' behaviors.


### Install dependencies:
```bash
pipenv install
pipenv shell

Author
Tandie Oyucho
