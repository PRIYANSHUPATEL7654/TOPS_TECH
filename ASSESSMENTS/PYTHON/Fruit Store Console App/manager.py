import json
import os
from utils import log_transaction, get_valid_integer, get_fruit_name

class Manager:
    FILE_NAME = "Fruit_Stock.json"

    def __init__(self):
        self.fruit_stock = self.load_data()

    def load_data(self):
        """Load fruit stock from JSON file"""
        if os.path.exists(self.FILE_NAME):
            try:
                with open(self.FILE_NAME, "r") as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return {}
        return {}

    def save_data(self):
        """Save current stock to JSON file"""
        with open(self.FILE_NAME, "w") as f:
            json.dump(self.fruit_stock, f, indent=4)

    def add_fruit_stock(self):
        """Add one or more fruits to stock (matches screenshot logic)"""
        fruit_count = get_valid_integer("\nEnter how many fruits you want to add: ")
        
        for _ in range(fruit_count):
            fruit_name = get_fruit_name("Enter fruit name: ")
            quantity = get_valid_integer("Enter quantity (in kg): ")
            price = get_valid_integer("Enter price (per kg): ")

            self.fruit_stock[fruit_name] = {"quantity": quantity, "price": price}
            print(f"✅ {fruit_name} added successfully!")

        self.save_data()
        log_transaction("Manager", "Add Fruit Stock", 
                       f"Added {fruit_count} fruit(s)")

    def view_fruit_stock(self):
        """Display all fruits in stock"""
        print("\n" + "="*50)
        print("                 FRUIT STOCK")
        print("="*50)
        
        if not self.fruit_stock:
            print("No fruit stock found.")
        else:
            for fruit_name, details in self.fruit_stock.items():
                print(f"Fruit name     : {fruit_name}")
                print(f"Quantity (kg)  : {details['quantity']}")
                print(f"Price (per kg) : ₹{details['price']}")
                print("-" * 40)
        
        log_transaction("Manager", "View Fruit Stock", "Viewed current stock")

    def update_fruit_stock(self):
        """Update quantity and price of existing fruit"""
        fruit_name = get_fruit_name("Enter fruit name to update: ")
        
        if fruit_name in self.fruit_stock:
            quantity = get_valid_integer("Enter new quantity (kg): ")
            price = get_valid_integer("Enter new price (per kg): ")

            self.fruit_stock[fruit_name] = {"quantity": quantity, "price": price}
            self.save_data()
            print("✅ Fruit updated successfully!")
            log_transaction("Manager", "Update Fruit Stock", 
                           f"Updated {fruit_name} → Qty={quantity}, Price={price}")
        else:
            print("❌ Fruit not found in stock.")

    def delete_fruit_stock(self):
        """Delete a fruit from stock"""
        fruit_name = get_fruit_name("Enter fruit name to delete: ")
        
        if fruit_name in self.fruit_stock:
            del self.fruit_stock[fruit_name]
            self.save_data()
            print("✅ Fruit deleted successfully!")
            log_transaction("Manager", "Delete Fruit Stock", f"Deleted {fruit_name}")
        else:
            print("❌ Fruit not found.")