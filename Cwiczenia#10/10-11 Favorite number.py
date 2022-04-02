## 10-11. Favorite Number: 
# 
# Write a program that prompts for the user’s favorite number. 
# 
# Use json.dump() to store this number in a file. 
# 
# Write a separate program that reads in this value and prints the message, 
#   “I know your favorite number! It’s _____.”

import json

def get_stored_number():
    """Get stored favorite number if possible."""
    filename = 'number.json'
    try:
        with open(filename) as f:
            number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return number

def get_new_number():
    """Prompt user for new favorite number."""
    number = input("What is your favorite number?: ")
    filename = 'number.json'
    with open(filename, 'w') as f:
        json.dump(number, f)
    return number

def display_number():
    """Show username his favorite number."""
    number = get_stored_number()
    if number:
        print(f"I know your favorite number! It is {number}.")
    else:
        number = get_new_number()
        print("I will remember your favorite number next time you come back!")

display_number()