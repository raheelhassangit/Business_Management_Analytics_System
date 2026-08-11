from app.customer import Customer

class CustomerManager:
    def __init__(self):
        self.customers = []

    def add_customer(self, customer):
        if isinstance(customer, Customer):
            self.customers.append(customer)
        else:
            raise ValueError("Invalid customer object")

    def remove_customer(self, customer_id):
        self.customers = [customer for customer in self.customers if customer.customer_id != customer_id]

    def get_customer(self, customer_id):
        for customer in self.customers:
            if customer.customer_id == customer_id:
                return customer
        return None

    def get_all_customers(self):
        return self.customers 
    
    def view_customer_info(self, customer_id):
        customer = self.get_customer(customer_id)
        if customer:
            print(f"Customer ID: {customer.customer_id}")
            print(f"Customer Name: {customer.name}")
            print(f"Customer Email: {customer.email}")
            print(f"Customer Phone: {customer.phone}")
            print(f"Customer Address: {customer.address}")
        else:
            print("Customer not found.")
    
    def view_all_customers_info(self):
        if not self.customers:
            print("No customers found.")
            return
        for customer in self.customers:
            self.view_customer_info(customer.customer_id)
            print("---")        