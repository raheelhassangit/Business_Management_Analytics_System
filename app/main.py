from app.customer_manager import CustomerManager
from app.physical_product import PhysicalProduct
from app.digital_product import DigitalProduct
from app.product_manager import ProductManager
from app.customer import Customer
from app.sale import Sale
from app.sale_manager import SaleManager


def main():
    product_manager = ProductManager()
    customer_manager = CustomerManager()
    sale_manager = SaleManager(
    customer_manager,
    product_manager
    )
    
    print("____ Welcome to Personal Finance & Business Management System ____")
    while True:
        print("\nPlease select an option:")
        print("1. Manage Customers")
        print("2. Manage Products")
        print("3. Manage Sales")
        print("4. Search Records")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Enter the option you want to perform:")
            print("1. Add Customer")
            print("2. Remove Customer")
            print("3. View Customer Information")
            print("4. View All Customers Information")
            
            customer_choice = input("Enter your choice: ")
            if customer_choice == "1":
                customer_id = int(input("Enter Customer ID: "))
                name = input("Enter Customer Name: ")
                email = input("Enter Customer Email: ")
                phone = input("Enter Customer Phone: ")
                address = input("Enter Customer Address: ")
                customer = Customer(customer_id, name, email, phone, address)
                customer_manager.add_customer(customer)
                print("Customer added successfully.")
            elif customer_choice == "2":
                customer_id = int(input("Enter Customer ID to remove: "))
                customer_manager.remove_customer(customer_id)
                print("Customer removed successfully.")
            elif customer_choice == "3":
                customer_id = int(input("Enter Customer ID to view: "))
                customer_manager.view_customer_info(customer_id)
            elif customer_choice == "4":
                customer_manager.view_all_customers_info()            
            
        elif choice == "2":
            print("Enter the option you want to perform:")
            print("1. Add Physical Product")
            print("2. Add Digital Product")
            print("3. View Product Information")
            print("4. View All Products Information")    
            product_choice = input("Enter your choice: ")
            if product_choice == "1":
                product_id = int(input("Enter the product ID:"))
                name = input("Enter the product name:")
                category = input("Enter the product category:")
                price = float(input("Enter the product price:"))
                quantity = int(input("Enter the product quantity:"))
                supplier = input("Enter the product supplier:")
                weight = float(input("Enter the product weight (in kg):"))
                physical_product = PhysicalProduct(product_id, name, category, price, quantity, supplier, weight)
                product_manager.add_product(physical_product)
                print("Physical product added successfully.")
            elif product_choice == "2":
                product_id = int(input("Enter the product ID:"))
                name = input("Enter the product name:")
                category = input("Enter the product category:")
                price = float(input("Enter the product price:"))
                quantity = int(input("Enter the product quantity:"))
                supplier = input("Enter the product supplier:")
                file_size = float(input("Enter the file size (in MB):"))
                download_link = input("Enter the download link:")
                digital_product = DigitalProduct(product_id, name, category, price, quantity, supplier, file_size, download_link)
                product_manager.add_product(digital_product)
                print("Digital product added successfully.")
            elif product_choice == "3":
                product_id = int(input("Enter the product ID to view:"))
                product = product_manager.get_product(product_id)
                if product:
                    product.display_product_info()
                else:
                    print("Product not found.")
            elif product_choice == "4":
                print("Physical Product Information:")
                for product in product_manager.get_all_products():
                    if isinstance(product, PhysicalProduct):
                        product.display_product_info()
                print("\nDigital Product Information:")
                for product in product_manager.get_all_products():
                    if isinstance(product, DigitalProduct):
                        product.display_product_info()            
        
        elif choice == "3":
            
            print("Enter the option you want to perform:")
            print("1. Record the sale")
            print("2. View sale")
            print("3. View all sales")
            sale_choice = input("Enter your choice: ")
            if sale_choice == "1":
                sale_id = int(input("Enter the sale ID:"))
                sale_customer_id = int(input("Enter the customer ID:"))
                sale_product_id = int(input("Enter the product ID:"))
                sale_quantity = int(input("Enter the quantity:"))
                sale_manager.record_sale(sale_id, sale_customer_id, sale_product_id, sale_quantity)
            elif sale_choice == "2":
                sale_id = int(input("Enter the sale ID:"))
                sale = sale_manager.get_sale(sale_id)
                if sale:
                    print("\n--- Sale Information ---")
                    print(f"Sale ID: {sale.sale_id}")
                    print(f"Customer: {sale.customer.name}")
                    print(f"Product: {sale.product.name}")
                    print(f"Quantity: {sale.quantity}")
                    print(f"Unit Price: ${sale.price:.2f}")
                    print(f"Total Price: ${sale.total_price:.2f}")
                else:
                    print("Sale not found.")
            elif sale_choice == "3":
                sales = sale_manager.get_all_sales()    
                if not sales:
                    print("No sales found.")
                else:
                    for sale in sales:
                        print("\n--- Sale Information ---")
                        print(f"Sale ID: {sale.sale_id}")
                        print(f"Customer: {sale.customer.name}")
                        print(f"Product: {sale.product.name}")
                        print(f"Quantity: {sale.quantity}")
                        print(f"Unit Price: ${sale.price:.2f}")
                        print(f"Total Price: ${sale.total_price:.2f}")            
        elif choice == "4":
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()