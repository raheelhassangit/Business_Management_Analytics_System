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

## Design Overview
Abstraction & Inheritance: Product is an abstract base class (ABC) defining a shared interface. PhysicalProduct and DigitalProduct inherit from it and implement calculate_shipping_cost() differently, demonstrating polymorphism.
Encapsulation: Product quantity is exposed as a validated property, rejecting negative or non-integer values at the point of assignment.
Separation of Concerns: Business logic (managers) is kept separate from the persistence layer (DataManager) and the reporting layer (ReportManager), following a manager-per-entity pattern.
Custom Exceptions: Domain-specific errors (InsufficientStockError, InvalidQuantityError) are raised instead of generic exceptions, making failure states explicit and catchable.
Manual Serialization: DataManager handles converting live objects to/from JSON, including reconstructing the correct product subclass (physical vs digital) on load.
Getting Started
Prerequisites
Python 3.10+
requests library
Installation
bash
pip install requests
Running the application
bash
python -m app.main
On startup, the app fetches a quote of the day and loads any existing data from data.json. On exit (option 6), current data is saved back to data.json.

Usage
The app runs an interactive menu:

1. Manage Customers
2. Manage Products
3. Manage Sales
4. Search Records
5. Generate Report
6. Exit
Each option opens a sub-menu for the relevant CRUD operations.

Known Limitations / Roadmap
This project is intentionally scoped as a fundamentals exercise, not a production system. Planned/possible improvements:

Input validation around console input() calls (currently assumes well-formed input)
Logging instead of print() for operational messages
Type hints across modules
Unit tests for manager and model logic
A future Django-based version of this same domain model, replacing the console layer with a proper web interface and ORM-backed persistence

## Author
### Raheel Hassan GitHub: raheelhassangit LinkedIn: raheel-hassan



