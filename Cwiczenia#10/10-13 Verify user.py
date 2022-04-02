##  10-13. Verify User: 
# 
# The final listing for remember_me.py assumes either that the user has 
#   already entered their username or that the program is running for the 
#       first time. 
# 
# We should modify it in case the current user is not the person who last 
#   used the program.
# 
# Before printing a welcome back message in greet_user(), ask the user if this 
#   is the correct username. 
# 
# If it’s not, call get_new_username() to get the correct username.

import json

def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def verify_user():
    """Verify if user is the same as the one that opened program previously."""
    username = get_stored_username()
    if username:
        prompt = f"Is your name {username}?"
        prompt += " Please type 'Yes' or 'No': "
        decision = input(prompt)
        return decision
    else:
        return None

def greet_user():
    decision = verify_user()
    username = get_stored_username()
    if decision == 'Yes':
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

greet_user()