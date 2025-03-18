import random
from datetime import datetime

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
    print("+" + "-"*50 + "+")
    
def welcome_page():
    separator()
    print(f"{"Welcome to AE Merchandise Store":^50}") #center justify
    separator()
    print(f"Transaction ID: {transaction_id():>35}") #right justify
    print(f"Date & Time: {date_time():>38}") #right justify
    separator()

def purchase_type():
    choice = input("Enter purchase type ('bulk' or 'retail'): ")
    return choice

def get_items():
    separator()
    item = input("Enter item: ")
    return item

def print_items():
    items_dict = {}
    try:  
        with open ("sampledict.csv") as file:
            for line in file:
                parts = [part.strip() for part in line.split(",")]
                if parts[0][0] == "#":
                    continue
                items_dict[parts[0]] = int(parts[1])
        #print choices
        # separator()
        print(f"{"Items":^25}|{"Price":^25}")
        separator()
        for key, value in items_dict.items():
            print(f"{key:<25}|              P{value:>10,.2f}")
        return items_dict
    
    except Exception as e:
        print(e)

    
def main():
    is_running = True
    welcome_page()
    print_items()
    
    separator()
    print("Enter 'q' to proceed checkout.")
    
    while is_running:
        while True:
            item = get_items()
            
            if item.lower() == 'q':
                choice = input("Proceed to checkout ('y' or 'n')? ")
                if choice == 'y':
                    break
                elif choice == 'n':
                    pass
            else:
                try:
                    choice = purchase_type()
                    if choice.lower() == 'bulk':
                        pass
                    elif choice.lower() == 'retail':
                        pass
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
                            print(f"{"Thank you for your purchase. Goodbye!":^50}") #center justify
                            separator()
                            is_running = False
                            break                        
                        else:
                            raise ValueError("Invalid choice")
                    except ValueError as ve:
                        print(f"Error: {ve}")

main()