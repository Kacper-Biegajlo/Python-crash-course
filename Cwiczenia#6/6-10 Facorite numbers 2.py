## 6-10. Favorite Numbers:

# Modify your program from Exercise 6-2 (page 99) 
#   so each person can have more than one favorite number. 
# Then print each person’s name along with their favorite numbers.

favorite_numbers = {
    'kaczor': ['69', '6969'],
    'vacool': ['420', '420420'],
    'niebieski': ['12', '1337'],
    'mc': ['1337', '1234'],
    'targen': ['0', '570'],
}

for name, number in favorite_numbers.items():
    print(f"{name.title()}'s favorite numbers are: {number}")
