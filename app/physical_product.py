from app.product import Product

class PhysicalProduct(Product):
    def __init__(self, product_id, name, category, price, quantity, supplier, weight):
        super().__init__(product_id, name, category, price, quantity, supplier)
        self.weight = weight
        
    def display_product_info(self):
            super().display_product_info()
            print(f"Product Weight: {self.weight} kg")
        
    def calculate_shipping_cost(self):
            base_shipping_cost = 5.0  # Base shipping cost in dollars
            weight_factor = 2.0  # Cost per kg
            shipping_cost = base_shipping_cost + (self.weight * weight_factor)
            return shipping_cost     
        