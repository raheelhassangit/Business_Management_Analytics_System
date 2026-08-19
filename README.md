# Business Management & Analytics System

A console-based business management system built in pure Python (OOP, no frameworks) to manage customers, products, and sales, with JSON-based persistence and live external API integration.

This project was built as a deliberate practice project to solidify core Python fundamentals — object-oriented design, abstraction, custom exceptions, and data serialization — before moving on to framework-based development (Django).

## Features
Customer Management — add, remove, view, and list customers
Product Management — supports two product types via inheritance:
PhysicalProduct — tracks weight, calculates shipping cost based on weight
DigitalProduct — tracks file size and download link, zero shipping cost
Sales Management — record sales against existing customers/products, with automatic stock deduction and total price calculation
Search — look up any customer, product, or sale by ID
Reporting — aggregate report covering customer count, inventory breakdown (physical vs. digital), total stock, inventory value, and total revenue
Persistence — all data is saved to and loaded from data.json between sessions
Quote of the Day — fetches a random quote from a public API on startup

## Project Structure
.
├── app/
│   ├── customer.py           # Customer data model (dataclass)
│   ├── customer_manager.py   # CRUD operations for customers
│   ├── product.py            # Abstract base Product class
│   ├── physical_product.py   # Physical product (weight-based shipping)
│   ├── digital_product.py    # Digital product (no shipping cost)
│   ├── product_manager.py    # CRUD operations for products
│   ├── sale.py                # Sale data model
│   ├── sale_manager.py       # Sale recording with stock validation
│   ├── report_manager.py     # Business analytics/report generation
│   ├── data_manager.py       # JSON save/load for all entities
│   ├── exceptions.py         # Custom exceptions (InsufficientStockError, InvalidQuantityError)
│   └── main.py                # CLI entry point and menu loop
├── API/
│   └── qoute_api.py          # Fetches a random quote from a public API
├── data.json                  # Persisted application data
├── requirements.txt
└── README.md