import random
import sys
from os import system
import sys
from datetime import datetime

inventory_dict = {}

def date_time():
    now = datetime.now()
    formatted_datetime = now.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_datetime

def transaction_id():
    characters = 'abcdefghijklmnopqrstuvwxyz'
    length = 8
    transaction_id = ''
    for i in range(length):
        transaction_id += random.choice(characters.upper())
    return transaction_id

def separator():
    print("+" + "-"*100 + "+")

def welcome_page():
    separator()
    print(f"{"Welcome to AE Merchandise Store":^100}") #center justify
    separator()
    print(f"Transaction ID: {transaction_id():>85}") #right justify
    print(f"Date & Time: {date_time():>88}") #right justify
    separator()

def purchase_type():
    choice = input("Enter purchase type ('bulk' or 'retail'): ")
    return choice

def get_item_input(category):
    separator()
    item = input("Select the item you want: ")
    quantity = input("Input quantity: ")
    for i, (key, value) in enumerate(inventory_dict[category].items()):
        if int(item) == i + 1:
            return key, int(quantity), int(quantity) * int(value)

def print_items(category):
    #Prints items listed inside category
    print(f"{"Items":^50}|{"Price":^50}")
    separator()
    for i, (key, value) in enumerate(inventory_dict[category].items()):
        value = "₱" + str(value)
        print(f"({i+1}) {key:<46}|{value:>50}")

def print_menu(): 
    separator()
    print(f"{"Menu":^100}")
    separator()
    for i, (key, value) in enumerate(inventory_dict.items()):
        print(f"({i+1}) {key}")

def get_menu_input() -> str:
    user_input = input(f"Select a category by inputting the number ('q' to checkout): ")
    for i, (key) in enumerate(inventory_dict):
        if not user_input.isalpha() and int(user_input) == i :
            return key
    return user_input

def process_items():
    try:
        with open ("products.csv") as file:
            for line in file:
                if line.strip():
                    parts = [part.strip() for part in line.split(",")]
                    if parts[0][0] == "#":
                        category = parts[0].replace("#", "")
                        inventory_dict[category] = {}
                        continue
                    inventory_dict[category][parts[0]] = float(parts[1])
    except Exception as e:
        print(e)

purchased_items = []

def apply_discount(total_cost, discount_rate=0.15):
    return total_cost * (1 - discount_rate)

def generate_receipt():
    separator()
    print(f"{"Receipt":^100}")
    separator()
    total_amount = 0
    for item, quantity, cost in purchased_items:
        print(f"{item:<50} x{quantity:<5} ₱{cost:>10}")
        total_amount += cost
    separator()
    print(f"{'Total Amount:':<55} ₱{total_amount:>10}")
    separator()

def main():
    is_running = True
    process_items()
    welcome_page()
    
    while is_running:
        while True:
            print_menu()
            menu_input = get_menu_input()
            
            if menu_input.isalpha() and menu_input.lower() == 'q':
                choice = input("Proceed to checkout ('y' or 'n')? ")
                if choice == 'y':
                    generate_receipt()
                    break
                elif choice == 'n':
                    continue
            else:
                try:
                    choice = purchase_type()
                    category = menu_input
                    if choice.lower() == 'bulk':
                        print_items(menu_input)
                        item, quantity, total_cost = get_item_input(category)
                        if quantity < 20:
                            print("Quantity is less than 20, no discount applied.")
                            print(f"Total cost: ₱{total_cost}")
                            purchased_items.append((item, quantity, total_cost))
                        else:
                            discounted_price = apply_discount(total_cost)
                            print(f"Total cost: ₱{total_cost}")
                            print(f"Discounted price: ₱{discounted_price}")
                            purchased_items.append((item, quantity, discounted_price))
                    elif choice.lower() == 'retail':
                        print_items(menu_input)
                        item, quantity, total_cost = get_item_input(category)
                        print(f"Total cost: ₱{total_cost}")
                        purchased_items.append((item, quantity, total_cost))
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
                    separator()
                    print(f"{"Thank you for your purchase. Goodbye!":^100}") #center justify
                    separator()
                    is_running = False
                    break                        
                else:
                    raise ValueError("Invalid choice")
            except ValueError as ve:
                print(f"Error: {ve}")

main()
# process_items()
# get_menu_input()