import json
import os
from utils import log_transaction, get_valid_integer, get_fruit_name


class Customer:
    FILE_NAME = "Fruit_Stock.json"
    FILE_NAME2 = "Fruit_Orders.json"

    def __init__(self):
        self.fruit_stock = self.load_data()
        self.cust_order = self.load_order()

    def load_data(self):
        if os.path.exists(self.FILE_NAME):
            try:
                with open(self.FILE_NAME, "r", encoding="utf-8") as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return {}
        return {}

    def load_order(self):
        if os.path.exists(self.FILE_NAME2):
            try:
                with open(self.FILE_NAME2, "r", encoding="utf-8") as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return {}
        return {}

    def save_data(self):
        with open(self.FILE_NAME, "w", encoding="utf-8") as f:
            json.dump(self.fruit_stock, f, indent=4)

    def save_order(self):
        with open(self.FILE_NAME2, "w", encoding="utf-8") as f:
            json.dump(self.cust_order, f, indent=4)

    def order_fruit(self):
        """Customer places order and stock is reduced"""
        print("\n" + "=" * 50)
        print("               AVAILABLE FRUITS")
        print("=" * 50)

        if not self.fruit_stock:
            print("No stock available.")
            return

        for name, d in self.fruit_stock.items():
            print(f"-> {name} | Qty: {d['quantity']} kg | Rs.{d['price']}/kg")

        fruit_name = get_fruit_name("\nEnter fruit you want to order: ")
        quantity = get_valid_integer("Enter quantity (kg): ")

        if fruit_name in self.fruit_stock:
            available = self.fruit_stock[fruit_name]["quantity"]
            price = self.fruit_stock[fruit_name]["price"]

            if quantity <= available:
                self.fruit_stock[fruit_name]["quantity"] -= quantity

                old_qty = self.cust_order.get(fruit_name, {}).get("quantity", 0)
                new_total_qty = old_qty + quantity
                total_bill = new_total_qty * price

                self.cust_order[fruit_name] = {
                    "quantity": new_total_qty,
                    "bill": total_bill,
                    "price": price,
                }

                self.save_data()
                self.save_order()

                print(f"Order placed! Total Bill = Rs.{total_bill}")
                log_transaction(
                    "Customer",
                    "Order Fruit",
                    f"Ordered {quantity} kg {fruit_name} | Total Qty={new_total_qty} | Bill=Rs.{total_bill}",
                )
            else:
                print("Not enough stock!")
        else:
            print("Fruit not available in stock.")

    def view_order(self):
        """Display customer's current orders"""
        print("\n" + "=" * 50)
        print("                 YOUR ORDERS")
        print("=" * 50)

        if not self.cust_order:
            print("No orders yet.")
        else:
            for name, d in self.cust_order.items():
                print(f"Fruit     : {name}")
                print(f"Quantity  : {d['quantity']} kg")
                print(f"Bill      : Rs.{d['bill']}")
                print("-" * 40)

        log_transaction("Customer", "View Order", "Viewed orders")

    def update_order(self):
        """Update existing order quantity"""
        fruit_name = get_fruit_name("Enter fruit name to update: ")

        if fruit_name not in self.cust_order:
            print("You have no order for this fruit.")
            return

        old_qty = self.cust_order[fruit_name]["quantity"]
        old_price = self.cust_order[fruit_name].get("price")
        in_stock = fruit_name in self.fruit_stock

        if in_stock:
            price = self.fruit_stock[fruit_name]["price"]
        elif old_price is not None:
            price = old_price
        else:
            print("This fruit is no longer in stock.")
            return

        new_qty = get_valid_integer("Enter new quantity (kg): ")

        if new_qty < old_qty:
            refund_qty = old_qty - new_qty
            if in_stock:
                self.fruit_stock[fruit_name]["quantity"] += refund_qty
        elif new_qty > old_qty:
            if not in_stock:
                print("This fruit is no longer in stock. Quantity cannot be increased.")
                return
            extra_needed = new_qty - old_qty
            if extra_needed > self.fruit_stock[fruit_name]["quantity"]:
                print("Not enough stock for increase.")
                return
            self.fruit_stock[fruit_name]["quantity"] -= extra_needed

        bill = new_qty * price
        self.cust_order[fruit_name] = {"quantity": new_qty, "bill": bill, "price": price}

        self.save_data()
        self.save_order()
        print("Order updated successfully!")
        log_transaction(
            "Customer",
            "Update Order",
            f"Updated {fruit_name} to {new_qty} kg | New Bill=Rs.{bill}",
        )

    def cancel_order(self):
        """Cancel order and restore stock"""
        fruit_name = get_fruit_name("Enter fruit name to cancel: ")

        if fruit_name in self.cust_order:
            qty = self.cust_order[fruit_name]["quantity"]
            price = self.cust_order[fruit_name].get("price")

            if fruit_name in self.fruit_stock:
                self.fruit_stock[fruit_name]["quantity"] += qty
            elif price is not None:
                self.fruit_stock[fruit_name] = {"quantity": qty, "price": price}

            del self.cust_order[fruit_name]
            self.save_data()
            self.save_order()
            print("Order cancelled successfully!")
            log_transaction("Customer", "Cancel Order", f"Cancelled {fruit_name} ({qty} kg)")
        else:
            print("You have no order for this fruit.")
