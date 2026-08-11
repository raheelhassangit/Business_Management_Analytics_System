from dataclasses import dataclass

@dataclass
class Customer:
    customer_id: int
    name: str
    email: str
    phone: str
    address: str    
        
        