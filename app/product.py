from app.exceptions import InsufficientStockError
from abc import ABC, abstractmethod

class Product(ABC):
    
    def __init__(self, product_id, name, category, price, quantity, supplier):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity
        self.supplier = supplier
    
    @property
    def quantity(self):
        return self._quantity
    @quantity.setter
    def quantity(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Quantity must be a non-negative integer.")
        self._quantity = value

    def display_product_info(self):
        print(f"Product ID: {self.product_id}")
        print(f"Product Name: {self.name}")
        print(f"Product Category: {self.category}")
        print(f"Product Price: ${self.price}")
        print(f"Product Quantity: {self.quantity}")
        print(f"Product Supplier: {self.supplier}")
    
    def update_price(self, new_price):
        if not isinstance(new_price, (int, float)) or new_price < 0:
            raise ValueError("Price must be a non-negative number.")
        self.price = new_price
        print(f"Product price updated to: ${self.price}")
        
    def add_stock(self, new_quantity):
        if not isinstance(new_quantity, int) or new_quantity <= 0:
            raise ValueError("New quantity must be a positive integer.")
        self.quantity += new_quantity
        print(f"Product stock updated to: {self.quantity} units")
    
    def remove_stock(self, quantity_to_remove):
        if not isinstance(quantity_to_remove, int) or quantity_to_remove <= 0:
            raise ValueError("Quantity to remove must be a positive integer.")
        if quantity_to_remove <= self.quantity:
            self.quantity -= quantity_to_remove
            print(f"Removed {quantity_to_remove} units from stock. New stock: {self.quantity} units")
        else:
            raise InsufficientStockError("Not enough stock to remove the requested quantity.")
        
    @abstractmethod
    def calculate_shipping_cost(self):
      ...    
        
                           
        
        
    
    