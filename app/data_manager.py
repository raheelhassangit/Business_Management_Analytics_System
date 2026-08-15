import json

import json

from app.customer import Customer
from app.physical_product import PhysicalProduct
from app.digital_product import DigitalProduct
from app.sale import Sale


class DataManager:

    def __init__(
        self,
        customer_manager,
        product_manager,
        sale_manager
    ):
        self.customer_manager = customer_manager
        self.product_manager = product_manager
        self.sale_manager = sale_manager

    def save_data(self, filename="data.json"):
        data = {
            "customers": [],
            "products": [],
            "sales": []
        }

        
        for customer in self.customer_manager.get_all_customers():
            data["customers"].append({
                "customer_id": customer.customer_id,
                "name": customer.name,
                "email": customer.email,
                "phone": customer.phone,
                "address": customer.address
            })

        
        for product in self.product_manager.get_all_products():

            if isinstance(product, PhysicalProduct):
                data["products"].append({
                    "product_id": product.product_id,
                    "name": product.name,
                    "category": product.category,
                    "price": product.price,
                    "quantity": product.quantity,
                    "supplier": product.supplier,
                    "type": "physical",
                    "weight": product.weight
                })

            elif isinstance(product, DigitalProduct):
                data["products"].append({
                    "product_id": product.product_id,
                    "name": product.name,
                    "category": product.category,
                    "price": product.price,
                    "quantity": product.quantity,
                    "supplier": product.supplier,
                    "type": "digital",
                    "file_size": product.file_size,
                    "download_link": product.download_link
                })

        
        for sale in self.sale_manager.get_all_sales():
            data["sales"].append({
                "sale_id": sale.sale_id,
                "customer_id": sale.customer.customer_id,
                "product_id": sale.product.product_id,
                "quantity": sale.quantity,
                "price": sale.price
            })

        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

        print(f"Data saved successfully to '{filename}'.")