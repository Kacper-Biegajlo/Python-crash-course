## 6-7. People: Start with the program you wrote for Exercise 6-1 (page 99).
# 
# Make two new dictionaries representing different people, 
#   and store all three dictionaries in a list called people. 
#  
# Loop through your list of people. As you loop through the list, 
#   print everything you know about each person.

chads = {
    'Kaczor': {
        'first_name': 'Dariusz',
        'last_name': 'Kaczyński', 
        'age': 'old',
        'city': 'Sławacinek Stary',
        'dick_size': 'too big',
    },
    'Mc': {
        'first_name': 'Patryk',
        'last_name': 'Jurkowski',
        'age': 'even older',
        'city': 'Biała Podlaska',
        'dick_size': 'on the fat size',
    },
    'Vacool': {
        'first_name': 'Grzegorz',
        'last_name':  'Wakuluk',
        'age': 'young',
        'city': 'Pruszków',
        'dick_size': 'perfection',
    }
}


for chad, chad_info in chads.items():
    print(f"\nChad: {chad}")
    full_name = f"{chad_info['first_name']} {chad_info['last_name']}"
    city = chad_info['city']
    age = chad_info['age']
    dick = chad_info['dick_size']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tCity: {city.title()}")
    print(f"\tAge: {age}")
    print(f"\tDick Size: {dick}")


###############################################################################

chads = {
    'Kaczor': {
        'first_name': 'Dariusz',
        'last_name': 'Kaczyński', 
        'age': 'old',
        'city': 'Sławacinek Stary',
        'dick_size': 'too big',
    },
    'Mc': {
        'first_name': 'Patryk',
        'last_name': 'Jurkowski',
        'age': 'even older',
        'city': 'Biała Podlaska',
        'dick_size': 'on the fat size',
    },
    'Vacool': {
        'first_name': 'Grzegorz',
        'last_name':  'Wakuluk',
        'age': 'young',
        'city': 'Pruszków',
        'dick_size': 'perfection',
    }
}


for chad, chad_info in chads.items():
    print(f"\nChad: {chad}")
    full_name = f"{chad_info['first_name']} {chad_info['last_name']}"

    print(f"\tFull name: {full_name.title()}")
    print(f"\tCity: {chad_info['city'].title()}")
    print(f"\tAge: {chad_info['age']}")
    print(f"\tDick Size: {chad_info['dick_size']}")

# wanted to try shorter version without variavles and it works Pog