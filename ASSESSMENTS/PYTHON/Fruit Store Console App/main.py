from manager import Manager
from customer import Customer

class Main:

    def __init__(self):
        pass

    def fruit_market(self):

        while True:
            try:
                print("\n\t\t\t\t\tWELCOME TO FRUIT MARKET")
                user_choice = int(input(
                    "\n\t\t\t\t\t1) Manager"
                    "\n\t\t\t\t\t2) Customer"
                    "\n\t\t\t\t\t3) Exit"
                    "\n\nEnter your choice from above options : "
                ))

                if user_choice == 1:
                    obj_manager = Manager()

                    print("\n\t\t\t\t\tWelcome Fruit Stock Manager")

                    while True:
                        try:
                            manager_choice = int(input(
                                "\n\t\t\t\t\t1) Add fruit stock\n"
                                "\t\t\t\t\t2) View fruit stock\n"
                                "\t\t\t\t\t3) Update fruit stock\n"
                                "\t\t\t\t\t4) Delete fruit stock\n"
                                "\t\t\t\t\t5) Exit\n"
                                "\nEnter your choice from above options : "
                            ))

                            if manager_choice == 1:
                                obj_manager.add_fruit_stock()

                            elif manager_choice == 2:
                                obj_manager.view_fruit_stock()

                            elif manager_choice == 3:
                                obj_manager.update_fruit_stock()

                            elif manager_choice == 4:
                                obj_manager.delete_fruit_stock()

                            elif manager_choice == 5:
                                break

                            else:
                                print("Invalid choice!")

                        except Exception as e:
                            print("Error occurred:", e)

                elif user_choice == 2:
                    obj_customer = Customer()

                    print("\n\t\t\t\t\tWelcome Fruit Stock Customer")

                    while True:
                        try:
                            customer_choice = int(input(
                                "\n\t\t\t\t\t1) Order fruit\n"
                                "\t\t\t\t\t2) View order\n"
                                "\t\t\t\t\t3) Update order\n"
                                "\t\t\t\t\t4) Cancel order\n"
                                "\t\t\t\t\t5) Exit\n"
                                "\nEnter your choice from above options : "
                            ))

                            if customer_choice == 1:
                                obj_customer.order_fruit()

                            elif customer_choice == 2:
                                obj_customer.view_order()

                            elif customer_choice == 3:
                                obj_customer.update_order()

                            elif customer_choice == 4:
                                obj_customer.cancel_order()

                            elif customer_choice == 5:
                                break

                            else:
                                print("Invalid choice!")

                        except Exception as e:
                            print("Error occurred:", e)

                elif user_choice == 3:
                    break

                else:
                    print("Invalid choice!")

            except Exception as e:
                print("Error occurred:", e)


obj_main = Main()
obj_main.fruit_market()
