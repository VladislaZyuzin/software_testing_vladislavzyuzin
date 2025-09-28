from .pepperoni import Pepperoni
from .barbecue import Barbecue
from .seafood import Seafood
from .order import Order

class Terminal:
    def __init__(self):
        self.order = Order()

    def show_menu(self):
        print("1. Pepperoni")
        print("2. Barbecue")
        print("3. Seafood")
        print("4. Confirm Order")
        print("5. Exit")

    def take_order(self):
        while True:
            self.show_menu()
            choice = input("Select a pizza or action by number: ")
            if choice == '1':
                self.order.add_pizza(Pepperoni())
                print("Pepperoni added to order!")
            elif choice == '2':
                self.order.add_pizza(Barbecue())
                print("Barbecue added to order!")
            elif choice == '3':
                self.order.add_pizza(Seafood())
                print("Seafood added to order!")
            elif choice == '4':
                print("Your order:")
                self.order.show_order()
                print(f"Total cost: {self.order.total_cost()} rubles.")
                break
            elif choice == '5':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
