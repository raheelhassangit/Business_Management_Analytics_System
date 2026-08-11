from app.product import Product

class DigitalProduct(Product):
    def __init__(self, product_id, name, category, price, quantity, supplier, file_size, download_link):
        super().__init__(product_id, name, category, price, quantity, supplier)
        self.file_size = file_size  # in MB
        self.download_link = download_link

    def display_product_info(self):
        super().display_product_info()
        print(f"File Size: {self.file_size} MB")
        print(f"Download Link: {self.download_link}")
    
    def calculate_shipping_cost(self):
        return 0.0  # Digital products have no shipping cost
        