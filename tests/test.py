from app.customer import Customer
from app.customer_manager import CustomerManager
from app.physical_product import PhysicalProduct
from app.product_manager import ProductManager
from app.sale_manager import SaleManager


def main():

    # -------------------------
    # Customer
    # -------------------------

    customer_manager = CustomerManager()

    customer = Customer(
        customer_id=123,
        name="Raheel",
        email="test@gmail.com",
        phone="03001234567",
        address="ABC, Lahore"
    )

    customer_manager.add_customer(customer)


    # -------------------------
    # Product
    # -------------------------

    product_manager = ProductManager()

    product = PhysicalProduct(
        product_id=123,
        name="Test",
        category="Tech",
        price=12.99,
        quantity=5,
        supplier="Random",
        weight=2.0
    )

    product_manager.add_product(product)


    # -------------------------
    # Sale Manager
    # -------------------------

    sale_manager = SaleManager(
        customer_manager,
        product_manager
    )


    # -------------------------
    # Record Sale
    # -------------------------

    sale = sale_manager.record_sale(
        sale_id=1,
        customer_id=123,
        product_id=123,
        quantity=2
    )


    # -------------------------
    # Sale Information
    # -------------------------

    print("\n--- Sale Information ---")
    print(f"Sale ID: {sale.sale_id}")
    print(f"Customer: {sale.customer.name}")
    print(f"Product: {sale.product.name}")
    print(f"Quantity: {sale.quantity}")
    print(f"Unit Price: ${sale.price:.2f}")
    print(f"Total Price: ${sale.total_price:.2f}")


    # -------------------------
    # Check Remaining Stock
    # -------------------------

    print(f"\nRemaining Stock: {product.quantity}")


    # -------------------------
    # Get Sale
    # -------------------------

    found_sale = sale_manager.get_sale(1)

    if found_sale:
        print("\nSale found successfully.")
    else:
        print("\nSale not found.")


if __name__ == "__main__":
    main()