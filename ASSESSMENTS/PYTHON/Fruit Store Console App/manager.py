import json
import os

class Manager:

    FILE_NAME = "Fruit_Stock.json"

    def __init__(self):
        self.fruit_stock = self.load_data()

    def load_data(self):
        if os.path.exists(self.FILE_NAME):
            try:
                with open(self.FILE_NAME, "r") as stock_data:
                    return json.load(stock_data)
            except json.JSONDecodeError:
                return {}
        return {}

    def save_data(self):
        with open(self.FILE_NAME, "w") as stock_data:
            json.dump(self.fruit_stock, stock_data, indent=4)

    def add_fruit_stock(self):

        fruit_count = int(input("\nEnter how many fruits you want to enter: "))

        for i in range(fruit_count):
            fruit_name = input("\nEnter fruit name: ").capitalize()
            quantity = int(input("Enter fruit quantity (in kg): "))
            price = int(input("Enter price (per kg): "))

            self.fruit_stock[fruit_name] = {
                "quantity": quantity,
                "price": price
            }

        self.save_data()
        print("Fruit/s added successfully!")

    def view_fruit_stock(self):
        print("\n\t\t\t\t\tFRUIT STOCK")

        if not self.fruit_stock:
            print("No fruit stock found.")
        else:
            for fruit_name, fruit_details in self.fruit_stock.items():
                print(f"\n\t\t\t\t\tFruit name : {fruit_name}")
                print(f"\t\t\t\t\t\tFruit quantity: {fruit_details['quantity']}")
                print(f"\t\t\t\t\t\tFruit price: {fruit_details['price']}")

    def update_fruit_stock(self):

        fruit_name = input("Enter fruit name to update: ").capitalize()

        if fruit_name in self.fruit_stock:
            quantity = int(input("Enter updated quantity: "))
            price = int(input("Enter updated price: "))

            self.fruit_stock[fruit_name] = {
                "quantity": quantity,
                "price": price
            }

            self.save_data()
            print("Fruit data updated successfully!")
        else:
            print("Fruit not found.")

    def delete_fruit_stock(self):

        fruit_name = input("Enter fruit name to delete: ").capitalize()

        if fruit_name in self.fruit_stock:
            del self.fruit_stock[fruit_name]
            print("Fruit data deleted successfully!")
        else:
            print(f"No fruit found with {fruit_name} name")