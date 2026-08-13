from app.product import Product


class ProductManager:

    def __init__(self):
        self.products = []

    def add_product(self, product):
        if not isinstance(product, Product):
            raise ValueError(
                "Only instances of Product or its subclasses can be added."
            )

        self.products.append(product)
        print(f"Product '{product.name}' added successfully.")

    def remove_product(self, product_id):
        if not isinstance(product_id, int):
            raise ValueError("Product ID must be an integer.")

        for product in self.products:
            if product.product_id == product_id:
                self.products.remove(product)
                print(
                    f"Product with ID {product_id} removed successfully."
                )
                return

        print(f"Product with ID {product_id} not found.")

    def get_product(self, product_id):
        if not isinstance(product_id, int):
            raise ValueError("Product ID must be an integer.")

        for product in self.products:
            if product.product_id == product_id:
                return product

        return None

    def get_all_products(self):
        if not isinstance(self.products, list):
            raise ValueError("Internal error: products is not a list.")

        return self.products