from app.product import Product
from app.customer import Customer


class Sale:

    def __init__(self, sale_id, product, customer, quantity, price):
        self.sale_id = sale_id
        self.product = product
        self.customer = customer
        self.quantity = quantity
        self.price = price

    @property
    def total_price(self):
        if not isinstance(self.quantity, int) or self.quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")

        if self.quantity > self.product.quantity:
            raise ValueError("Not enough stock available for the requested quantity.")

        return self.price * self.quantity