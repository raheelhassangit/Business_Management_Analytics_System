from app.physical_product import PhysicalProduct
from app.digital_product import DigitalProduct

class Reportmanager:
    def __init__(self, customer_manager, product_manager, sale_manager):
        self.customer_manager = customer_manager
        self.product_manager = product_manager
        self.sale_manager = sale_manager

    def generate_report(self):
        customers = self.customer_manager.get_all_customers()
        products = self.product_manager.get_all_products()
        sales = self.sale_manager.get_all_sales()

        total_customers = len(customers)
        total_products = len(products)

        physical_products = sum(
            isinstance(product, PhysicalProduct)
            for product in products
        )

        digital_products = sum(
            isinstance(product, DigitalProduct)
            for product in products
        )

        total_stock = sum(
            product.quantity
            for product in products
        )

        inventory_value = sum(
            product.price * product.quantity
            for product in products
        )

        total_sales = len(sales)

        total_items_sold = sum(
            sale.quantity
            for sale in sales
        )

        total_revenue = sum(
            sale.total_price
            for sale in sales
        )

        print("\n" + "=" * 45)
        print("       BUSINESS MANAGEMENT REPORT")
        print("=" * 45)

        print("\n--- Customers ---")
        print(f"Total Customers: {total_customers}")

        print("\n--- Products ---")
        print(f"Total Products: {total_products}")
        print(f"Physical Products: {physical_products}")
        print(f"Digital Products: {digital_products}")
        print(f"Total Stock: {total_stock}")
        print(f"Inventory Value: ${inventory_value:.2f}")

        print("\n--- Sales ---")
        print(f"Total Sales: {total_sales}")
        print(f"Total Items Sold: {total_items_sold}")
        print(f"Total Revenue: ${total_revenue:.2f}")

        print("\n" + "=" * 45)