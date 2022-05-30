## 6-8. Pets: 
# Make several dictionaries, where each dictionary represents a different pet.
# In each dictionary, include the kind of animal and the owner’s name. 
# Store these dictionaries in a list called pets. 
# Next, loop through your list and as you do, 
#   print everything you know about each pet.

Benek = {
    'name': 'Benek',
    'animal': 'cat',
    'owner': 'Beata',
}

Moskwa = {
    'name': 'Moskwa',
    'animal': 'cat',
    'owner': 'Niebieski'
}

Pog = {
    'name': 'Pog',
    'animal': 'dog',
    'owner': 'Kaczor',
}

Ginger = {
    'name': 'Ginger',
    'animal': 'fish',
    'owner': 'Vacool',
}

pets = [Benek, Moskwa, Pog, Ginger]

for pet in pets:
    print(f"\n{pet['owner']} has a {pet['animal']} called {pet['name']}.")
    