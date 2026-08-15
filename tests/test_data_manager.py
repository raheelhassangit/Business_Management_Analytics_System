from app.customer import Customer
from app.customer_manager import CustomerManager
from app.physical_product import PhysicalProduct
from app.digital_product import DigitalProduct
from app.product_manager import ProductManager
from app.sale_manager import SaleManager
from app.data_manager import DataManager


def main():

    customer_manager = CustomerManager()
    product_manager = ProductManager()

    sale_manager = SaleManager(
        customer_manager,
        product_manager
    )

    data_manager = DataManager(
        customer_manager,
        product_manager,
        sale_manager
    )

    # Customers
    customer1 = Customer(
        customer_id=123,
        name="Raheel",
        email="test@gmail.com",
        phone="03001234567",
        address="ABC, Lahore"
    )

    customer2 = Customer(
        customer_id=456,
        name="Hassan",
        email="test1@gmail.com",
        phone="03001234567",
        address="DEF, Lahore"
    )

    customer_manager.add_customer(customer1)
    customer_manager.add_customer(customer2)

    # Physical Product
    physical_product = PhysicalProduct(
        product_id=123,
        name="Laptop",
        category="Tech",
        price=12.99,
        quantity=5,
        supplier="Random",
        weight=2.0
    )

    # Digital Product
    digital_product = DigitalProduct(
        product_id=456,
        name="Ebook",
        category="Education",
        price=12.99,
        quantity=5,
        supplier="Random",
        file_size=1.0,
        download_link="https://test.com"
    )

    product_manager.add_product(physical_product)
    product_manager.add_product(digital_product)

    # Sales
    sale_manager.record_sale(
        sale_id=1,
        customer_id=123,
        product_id=123,
        quantity=2
    )

    sale_manager.record_sale(
        sale_id=2,
        customer_id=456,
        product_id=456,
        quantity=1
    )

    # Save
    data_manager.save_data()
    data_manager.load_data("data.json")
    print("\n--- Sales ---")

    sales = sale_manager.get_all_sales()

    print(f"Total Sales: {len(sales)}")

    for sale in sales:
        print(
            f"Sale ID: {sale.sale_id} | "
            f"Customer: {sale.customer.name} | "
            f"Product: {sale.product.name} | "
            f"Quantity: {sale.quantity} | "
            f"Total: ${sale.total_price:.2f}"
        )

    # ---------------- RELATIONSHIP TEST ----------------

    print("\n--- Relationship Verification ---")
    customers = customer_manager.get_all_customers()
    products = product_manager.get_all_products()

    for sale in sales:

        customer_exists = sale.customer in customers
        product_exists = sale.product in products

        print(
            f"Sale {sale.sale_id}: "
            f"Customer linked = {customer_exists}, "
            f"Product linked = {product_exists}"
        )

    print("\n=============================================")
    print("       DATA VERIFICATION COMPLETED")
    print("=============================================")



if __name__ == "__main__":
    main()