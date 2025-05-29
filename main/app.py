import random
import pandas as pd
from datetime import datetime
 
class Warehouse:
    def __init__(self):
        self.inventory: pd.DataFrame = pd.DataFrame()
        self.purchased_items = []

    def date_time(self):
        #Returns current date time
        now = datetime.now()
        formatted_datetime = now.strftime("%Y-%m-%d %H:%M:%S")
        return formatted_datetime

    def transaction_id(self):
        #Returns a randomly generated id
        characters = 'abcdefghijklmnopqrstuvwxyz'
        length = 8
        transaction_id = ''
        for i in range(length):
            transaction_id += random.choice(characters.upper())
        return transaction_id

    def separator(self):
        print("+" + "-"*100 + "+")

    def welcome_page(self, transaction_id: str):
        #Prints a welcome page with transaction id and current date
        self.separator()
        print(f"{"Welcome to AE Merchandise Store":^100}") #center justify
        self.separator()
        print(f"Transaction ID: {transaction_id:>85}") #right justify
        print(f"Date & Time: {self.date_time():>88}") #right justify
        self.separator()

    def purchase_type(self):
        # Returns either bulk or retail as the purchase type
        # Input Validation
        try: 
            choice = input("Enter purchase type ('bulk' or 'retail'): ")
            if choice not in['bulk', 'retail']:
                raise ValueError("Invalid Input: Please only enter 'bulk' or 'retail'")
            return choice
        except ValueError as ve:
            print(ve)
            return self.purchase_type()

    def get_item_input(self, category):
        # Gets item input from user based on the arguments given
        # and returns the item name, quantity of item and its total price
        items = self.inventory[self.inventory["Category"] == category]
        items = tuple(items[['Product Name', 'Price']].itertuples(index=False,name=None))
        self.separator()
        while True:  # input validation
           item = input("Select the item you want: ").strip()
           if not item.isdigit():
               print("Invalid input. Please enter a valid item number.")
               continue
           item = int(item)
            
           if item < 1 or item > len(items):
               print("Invalid item selection. Please choose a valid item.")
               continue
            
           quantity = input("Input quantity: ").strip()
           if not quantity.isdigit() or int(quantity) < 1:
               print("Invalid quantity. Please enter a positive integer.")
               continue
            
           quantity = int(quantity)
           for i, value in enumerate(items):
               if item == i + 1:
                   return value[0], quantity, quantity * value[1], value[1]

    def print_items(self, category):
        #Prints items listed inside category
        print(f"{"Items":^50}|{"Price":^50}")
        self.separator()
        category_items = self.inventory[self.inventory["Category"] == category]
        category_items = tuple(category_items[['Product Name','Price']].itertuples(index=False,name=None))
        
        for i, items in enumerate(category_items):
            value = "₱" + str(items[1])
            print(f"({i+1}) {items[0]:<46}|{value:>50}")

    def print_menu(self): 
        #Prints menu options
        self.separator()
        print(f"{"Menu":^100}")
        self.separator()
        categories = self.inventory['Category'].unique()
        for i, items in enumerate(categories):
            print(f"({i+1}) {items}")

    def get_menu_input(self) -> str:
        # Get the input of the user or press q to quit
        categories = self.inventory["Category"].unique()
        while True:  
           user_input = input(f"Select a category by inputting the number ('q' to checkout): ").strip()
           if user_input.lower() == 'q':
               return user_input
           if not user_input.isdigit() or int(user_input) < 1 or int(user_input) > len(categories):
               print("Invalid input. Please enter a valid category number or 'q' to checkout.")
               continue
            
           for i, key in enumerate(categories):
               if int(user_input) == i + 1:
                   return key
                    
    def process_items(self):
        self.inventory = pd.read_csv('../products.csv', header=0)
        return self.inventory

    def apply_discount(self, total_cost, discount_rate=0.15):
        #Return a discounted version of the cost
        return total_cost * (1 - discount_rate)

    def generate_receipt(self):
        #Generates the receipt which includes the item quantity, and cost of the item
        self.separator()
        print(f"{"Receipt":^100}")
        self.separator()
        total_amount = 0
        for item in self.purchased_items:
            item_name, quantity, cost, *_ = item 
            total_amount += cost
            cost = '₱' + str(f"{cost:.2f}")
            print(f"{quantity:^10}{item_name:<50}{cost:>41}")
        self.separator()
        total_amount = '₱' + str(f"{total_amount:.2f}") 
        print(f"{'Total Amount:':<60} {total_amount:>40}")
        self.separator()

    def print_cart(self):
        max_length = 24
        self.separator() 
        print(f"{'Cart':^100}")
        self.separator()
        print(f"{'Qty':^25}|{'Item':^25}|{'Unit Price':^25}|{'Total Cost':^25}")
        self.separator()
        for item in self.purchased_items:
            item_name = f"{item[0][0:max_length-4]}..." if len(item[0]) > max_length else item[0] 
            price_per_unit = "₱" + str(f"{item[3]:.2f}") 
            total_cost = "₱" + str(f"{item[2]:.2f}")

            print(f"{item[1]:^25}|{item_name:^25}|{price_per_unit:^25}|{total_cost:^25}")

    def main(self):
        is_running = True
        transaction_id_instance = self.transaction_id()
        self.process_items()
        while is_running:
            while True:
                self.welcome_page(transaction_id_instance)
                if self.purchased_items:
                    self.print_cart()
                self.print_menu()
                menu_input = self.get_menu_input()
                
                if menu_input.isalpha() and menu_input.lower() == 'q':
                    choice = input("Proceed to checkout ('y' or 'n')? ")
                    if choice == 'y':
                        self.generate_receipt()
                        break
                    elif choice == 'n':
                        continue
                else:
                    try:
                        choice = self.purchase_type()
                        category = menu_input
                        if choice.lower() == 'bulk':
                            self.print_items(category)
                            item, quantity, total_cost, price_per_unit = self.get_item_input(category)
                            if quantity < 20:
                                print("Quantity is less than 20, no discount applied.")
                                print(f"Total cost: ₱{total_cost}")
                                discounted = False
                                self.purchased_items.append((item, quantity, total_cost, price_per_unit, discounted))
                            else:
                                discounted_price = self.apply_discount(total_cost)
                                print(f"Total cost: ₱{total_cost:.2f}")
                                print(f"Discounted price: ₱{discounted_price:.2f}")
                                discounted = True
                                self.purchased_items.append((item, quantity, discounted_price, price_per_unit, discounted))
                        elif choice.lower() == 'retail':
                            self.print_items(menu_input)
                            item, quantity, total_cost, price_per_unit = self.get_item_input(category)
                            print(f"Total cost: ₱{total_cost}")
                            discounted = False
                            self.purchased_items.append((item, quantity, total_cost, price_per_unit, discounted))
                        else:
                            raise ValueError("Invalid purchase type")
                    except ValueError as ve:
                        print(f"Error: {ve}")
                    
            while True:
                buy_again = input("\nWould you like to add something ('y' or 'n')? ")
                try:
                    if buy_again.lower() == 'y':
                        print()
                        break
                    elif buy_again.lower() == 'n':
                        self.separator()
                        print(f"{"Thank you for your purchase. Goodbye!":^100}") #center justify
                        self.separator()
                        is_running = False
                        break                        
                    else:
                        raise ValueError("Invalid choice")
                except ValueError as ve:
                    print(f"Error: {ve}")
# process_items()
# get_menu_input()
warehouse = Warehouse()
warehouse.main()
