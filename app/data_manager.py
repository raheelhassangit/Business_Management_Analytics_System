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

    def load_data(self, filename="data.json"):

        try:
            with open(filename, "r") as file:
                data = json.load(file)

        except FileNotFoundError:
            print(f"'{filename}' not found. Starting with empty data.")
            return


        self.customer_manager.customers.clear()
        self.product_manager.products.clear()
        self.sale_manager.sales.clear()



        for customer_data in data.get("customers", []):

            customer = Customer(
                customer_id=customer_data["customer_id"],
                name=customer_data["name"],
                email=customer_data["email"],
                phone=customer_data["phone"],
                address=customer_data["address"]
            )

            self.customer_manager.add_customer(customer)


        for product_data in data.get("products", []):

            if product_data["type"] == "physical":

                product = PhysicalProduct(
                    product_id=product_data["product_id"],
                    name=product_data["name"],
                    category=product_data["category"],
                    price=product_data["price"],
                    quantity=product_data["quantity"],
                    supplier=product_data["supplier"],
                    weight=product_data["weight"]
                )

            elif product_data["type"] == "digital":

                product = DigitalProduct(
                    product_id=product_data["product_id"],
                    name=product_data["name"],
                    category=product_data["category"],
                    price=product_data["price"],
                    quantity=product_data["quantity"],
                    supplier=product_data["supplier"],
                    file_size=product_data["file_size"],
                    download_link=product_data["download_link"]
                )

            else:
                print(
                    f"Unknown product type: "
                    f"{product_data['type']}"
                )
                continue

            self.product_manager.add_product(product)


        for sale_data in data.get("sales", []):

            customer = self.customer_manager.get_customer(
                sale_data["customer_id"]
            )

            product = self.product_manager.get_product(
                sale_data["product_id"]
            )

            if customer is None or product is None:
                print(
                    f"Skipping sale {sale_data['sale_id']}: "
                    "customer or product not found."
                )
                continue

            sale = Sale(
                sale_id=sale_data["sale_id"],
                product=product,
                customer=customer,
                quantity=sale_data["quantity"],
                price=sale_data["price"]
            )

            self.sale_manager.sales.append(sale)

        print(f"Data loaded successfully from '{filename}'.")