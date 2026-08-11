from app.sale import Sale
from app.customer_manager import CustomerManager
from app.product_manager import ProductManager
from app.exceptions import InsufficientStockError, InvalidQuantityError

class SaleManager:
    def __init__(self, customer_manager, product_manager):
        self.sales = []
        self.customer_manager = customer_manager
        self.product_manager = product_manager
    
    def record_sale(self, sale_id, customer_id, product_id, quantity):
        customer = self.customer_manager.get_customer(customer_id)
        if customer is None:
            raise ValueError(f"Customer with ID {customer_id} not found.")
        
        product = self.product_manager.get_product(product_id)
        if product is None:
            raise ValueError(f"Product with ID {product_id} not found.")
        
        if not isinstance(quantity, int) or quantity <= 0:
            raise InvalidQuantityError("Quantity must be a positive integer.")
        
        if quantity > product.quantity:
            raise InsufficientStockError(
                f"Not enough stock for product '{product.name}'. "
                f"Available: {product.quantity}, Requested: {quantity}"
            )
            
        sale = Sale(
            sale_id=sale_id,
            product=product,
            customer=customer,
            quantity=quantity,
            price=product.price
        )
        
        product.quantity -= quantity
        self.sales.append(sale)
        print(
            f"Sale recorded successfully. "
            f"Total price: ${sale.total_price:.2f}"
        )
        return sale    
            
        
    def get_sale(self, sale_id):
        for sale in self.sales:
            if sale.sale_id == sale_id:
                return sale
        return None
        
    def get_all_sales(self):
        return self.sales        