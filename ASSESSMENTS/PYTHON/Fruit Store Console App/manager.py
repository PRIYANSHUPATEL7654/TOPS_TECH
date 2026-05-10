import json
import os
from utils import log_transaction, get_valid_integer, get_fruit_name


class Manager:
    FILE_NAME = "Fruit_Stock.json"
    ORDER_FILE_NAME = "Fruit_Orders.json"

    def __init__(self):
        self.fruit_stock = self.load_data()

    def load_data(self):
        """Load fruit stock from JSON file"""
        if os.path.exists(self.FILE_NAME):
            try:
                with open(self.FILE_NAME, "r", encoding="utf-8") as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return {}
        return {}

    def load_orders(self):
        """Load customer orders to validate stock delete safety"""
        if os.path.exists(self.ORDER_FILE_NAME):
            try:
                with open(self.ORDER_FILE_NAME, "r", encoding="utf-8") as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return {}
        return {}

    def save_data(self):
        """Save current stock to JSON file"""
        with open(self.FILE_NAME, "w", encoding="utf-8") as f:
            json.dump(self.fruit_stock, f, indent=4)

    def add_fruit_stock(self):
        """Add one or more fruits to stock"""
        fruit_count = get_valid_integer("\nEnter how many fruits you want to add: ")

        for _ in range(fruit_count):
            fruit_name = get_fruit_name("Enter fruit name: ")
            quantity = get_valid_integer("Enter quantity (in kg): ")
            price = get_valid_integer("Enter price (per kg): ")

            if fruit_name in self.fruit_stock:
                self.fruit_stock[fruit_name]["quantity"] += quantity
                self.fruit_stock[fruit_name]["price"] = price
                print(f"{fruit_name} stock updated successfully!")
            else:
                self.fruit_stock[fruit_name] = {"quantity": quantity, "price": price}
                print(f"{fruit_name} added successfully!")

        self.save_data()
        log_transaction("Manager", "Add Fruit Stock", f"Added/updated {fruit_count} fruit(s)")

    def view_fruit_stock(self):
        """Display all fruits in stock"""
        print("\n" + "=" * 50)
        print("                 FRUIT STOCK")
        print("=" * 50)

        if not self.fruit_stock:
            print("No fruit stock found.")
        else:
            for fruit_name, details in self.fruit_stock.items():
                print(f"Fruit name     : {fruit_name}")
                print(f"Quantity (kg)  : {details['quantity']}")
                print(f"Price (per kg) : Rs.{details['price']}")
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
            print("Fruit updated successfully!")
            log_transaction(
                "Manager",
                "Update Fruit Stock",
                f"Updated {fruit_name} -> Qty={quantity}, Price={price}",
            )
        else:
            print("Fruit not found in stock.")

    def delete_fruit_stock(self):
        """Delete a fruit from stock if it is not part of active orders"""
        fruit_name = get_fruit_name("Enter fruit name to delete: ")

        if fruit_name in self.fruit_stock:
            orders = self.load_orders()
            if fruit_name in orders and orders[fruit_name].get("quantity", 0) > 0:
                print("Cannot delete. This fruit has an active customer order.")
                return

            del self.fruit_stock[fruit_name]
            self.save_data()
            print("Fruit deleted successfully!")
            log_transaction("Manager", "Delete Fruit Stock", f"Deleted {fruit_name}")
        else:
            print("Fruit not found.")
