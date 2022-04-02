## 10-12. Favorite Number Remembered: 
# 
# Combine the two programs from Exercise 10-11 into one file. 
# 
# If the number is already stored, report the favorite number to the user. 
# 
# If not, prompt for the user’s favorite number and store it in a file. 
# 
# Run the program twice to see that it works.

# IM SORRY IM DUMB ALREADY DID IT THIS WAY IN 10-11...

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