from manager import Manager
from customer import Customer
from utils import log_transaction, get_valid_integer, get_fruit_name

class Main:
    def fruit_market(self):
        """Main controller - displays role menu and runs until user exits"""
        while True:
            try:
                print("\n" + "="*70)
                print("                    WELCOME TO FRUIT MARKET")
                print("="*70)
                
                choice = get_valid_integer(
                    "\n1) Manager\n"
                    "2) Customer\n"
                    "3) Exit\n\n"
                    "Select your Role : ", min_value=1
                )

                if choice == 1:
                    self.run_manager()
                elif choice == 2:
                    self.run_customer()
                elif choice == 3:
                    print("\nThank you for using Fruit Market! 👋")
                    break
                else:
                    print("Invalid choice!")

            except Exception as e:
                print(f"Unexpected error: {e}. Returning to main menu.")

    def run_manager(self):
        obj = Manager()
        print("\n" + "="*50)
        print("             FRUIT MARKET MANAGER")
        print("="*50)
        
        while True:
            try:
                ch = get_valid_integer(
                    "\n1) Add Fruit Stock\n"
                    "2) View Fruit Stock\n"
                    "3) Update Fruit Stock\n"
                    "4) Delete Fruit Stock\n"
                    "5) Exit to Main Menu\n\n"
                    "Enter your choice : ", min_value=1
                )

                if ch == 1:    obj.add_fruit_stock()
                elif ch == 2:  obj.view_fruit_stock()
                elif ch == 3:  obj.update_fruit_stock()
                elif ch == 4:  obj.delete_fruit_stock()
                elif ch == 5:  break
                else:
                    print("Invalid choice!")

            except Exception as e:
                print(f"Error: {e}. Returning to Manager menu.")

    def run_customer(self):
        obj = Customer()
        print("\n" + "="*50)
        print("             FRUIT MARKET CUSTOMER")
        print("="*50)
        
        while True:
            try:
                ch = get_valid_integer(
                    "\n1) Order Fruit\n"
                    "2) View Order\n"
                    "3) Update Order\n"
                    "4) Cancel Order\n"
                    "5) Exit to Main Menu\n\n"
                    "Enter your choice : ", min_value=1
                )

                if ch == 1:    obj.order_fruit()
                elif ch == 2:  obj.view_order()
                elif ch == 3:  obj.update_order()
                elif ch == 4:  obj.cancel_order()
                elif ch == 5:  break
                else:
                    print("Invalid choice!")

            except Exception as e:
                print(f"Error: {e}. Returning to Customer menu.")


# ================== START PROGRAM ==================
if __name__ == "__main__":
    Main().fruit_market()