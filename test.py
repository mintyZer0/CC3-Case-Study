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
    print(f"Date & Time: {date_time():>38}\n") #right justify
    separator()

def purchase_type():
    choice = input("Enter purchase type ('bulk' or 'retail'): ")
    return choice

def number_of_items():
    n = int(input("Enter number of items: "))
    return n
    
def main():
    is_running = True
    welcome_page()
    
    while is_running:
        n = number_of_items()
        
        for i in range(1, (n + 1)):
            
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