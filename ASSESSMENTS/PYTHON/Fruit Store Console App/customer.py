import json
import os


class Customer:

    FILE_NAME = "Fruit_Stock.json"
    FILE_NAME2 = "Fruit_Orders.json"

    def __init__(self):
        self.fruit_stock = self.load_data()
        self.cust_order = self.load_order()

    def load_data(self):
        if os.path.exists(self.FILE_NAME):
            try:
                with open(self.FILE_NAME, "r") as stock_data:
                    return json.load(stock_data)
            except json.JSONDecodeError:
                return {}
        return {}
    
    def load_order(self):
        if os.path.exists(self.FILE_NAME2):
            try:
                with open(self.FILE_NAME2, "r") as order_data:
                    return json.load(order_data)
            except json.JSONDecodeError:
                return {}
        return {}

    def save_data(self):
        with open(self.FILE_NAME, "w") as stock_data:
            json.dump(self.fruit_stock, stock_data, indent=4)

    def save_order(self):
        with open(self.FILE_NAME2,"w") as order_data:
            json.dump(self.cust_order, order_data, indent=4)

    def order_fruit(self):

        print("\nFruits in Current Stock")

        if not self.fruit_stock:
            print("No fruit stock found.")
        else:
            for fruit_name, fruit_details in self.fruit_stock.items():
                print(f"\n\t\t\t\t\tFruit name: {fruit_name}")
                print(f"\t\t\t\t\t\tFruit quantity: {fruit_details['quantity']}")
                print(f"\t\t\t\t\t\tFruit price: {fruit_details['price']}")
        
        fruit_name = input("\nEnter the fruit you want to order : ").capitalize()
        fruit_quantity = int(input("Enter the quantity of fruit : "))

        if fruit_name in self.fruit_stock:

            available_quantity = self.fruit_stock[fruit_name]["quantity"]
            price = self.fruit_stock[fruit_name]["price"]

            if fruit_quantity <= available_quantity:

                total_bill = fruit_quantity * price
                self.fruit_stock[fruit_name]["quantity"] -= fruit_quantity

                self.cust_order[fruit_name] = {"quantity" : fruit_quantity, "bill" : total_bill}

                self.save_data()
                self.save_order()

                print(f"Your total bill is : {total_bill}")

            else:
                print("Not enough stock for accomplishing order")

        else:
            print("Sorry sir/mam, right now the fruit does not exist in our stock")

    def view_order(self):
        print("\n\t\t\t\t\tYour Order/s")

        if not self.cust_order:
            print("\t\t\t\t\tNo orders found.")
        else:
            for fruit_name, order_details in self.cust_order.items():
                print(f"\n\t\t\t\t\tFruit name : {fruit_name}")
                print(f"\t\t\t\t\t\tFruit quantity : {order_details['quantity']}")
                print(f"\t\t\t\t\t\tTotal bill : {order_details['bill']}")

    def update_order(self):

        fruit_name = input("\nEnter fruit name to update your order : ").capitalize()
        price = self.fruit_stock[fruit_name]["price"]

        if fruit_name in self.cust_order:

            order_quantity = int(input("Enter non zero quantity of order to update : "))
            available_quantity = self.fruit_stock[fruit_name]["quantity"]
            ordered_quantity = self.cust_order[fruit_name]["quantity"]
            
            if order_quantity < ordered_quantity:

                self.cust_order[fruit_name]["quantity"] = order_quantity
                reduced_fruit_stock_quantity = ordered_quantity - order_quantity
                self.fruit_stock[fruit_name]["quantity"] += reduced_fruit_stock_quantity

            elif order_quantity > ordered_quantity:
                
                increased_fruit_stock_quantity = order_quantity - ordered_quantity

                if increased_fruit_stock_quantity <= available_quantity:

                    self.fruit_stock[fruit_name]["quantity"] -= increased_fruit_stock_quantity
                    self.cust_order[fruit_name]["quantity"] = order_quantity

                else:

                    print("The updated quantity is more than the stock quantity, so it cannot be updated")
                    return
                
            bill = order_quantity * price

            self.cust_order[fruit_name] = {
                "quantity": order_quantity,
                "bill": bill
            }

            self.save_data()
            self.save_order()

            print("Fruit data updated successfully!")
        else:
            print("Fruit not found.")

    def cancel_order(self):

        fruit_name = input("Enter fruit name to delete your order : ").capitalize()
        ordered_quantity = self.cust_order[fruit_name]["quantity"]
        self.fruit_stock[fruit_name]["quantity"] += ordered_quantity
        del self.cust_order[fruit_name]
        self.save_data()
        self.save_order()
        print("Order cancelled successfully!")
