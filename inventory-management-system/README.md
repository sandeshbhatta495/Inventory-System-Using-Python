# Inventory Management System

## Overview
The Inventory Management System is a Python-based application designed to help users manage product inventories efficiently. It allows users to view available products, search for specific items, add products to a shopping cart, and generate invoices upon checkout.

## Features
- Load and display products from a CSV file.
- Search for products by name.
- Add products to a shopping cart with quantity management.
- Calculate total costs of items in the cart.
- Save invoices to a CSV file.

## Project Structure
```
inventory-management-system
├── src
│   ├── inventory_store.py      # Main logic for the inventory management system
│   └── utils
│       └── __init__.py         # Utility functions (currently empty)
├── data
│   └── products.csv            # Product data in CSV format
├── requirements.txt             # Project dependencies
└── README.md                    # Project documentation
```

## Setup Instructions
1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies using the following command:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Ensure that the `products.csv` file is present in the `data` directory and contains the necessary product information.
2. Run the application using the command:
   ```
   python src/inventory_store.py
   ```
3. Follow the on-screen prompts to interact with the inventory management system.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

