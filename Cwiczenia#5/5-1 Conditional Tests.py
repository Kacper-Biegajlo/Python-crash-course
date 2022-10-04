## 5-1. Conditional Tests: Write a series of conditional tests. 
#   Print a statement describing each test and your prediction for the 
#       results of each test. Your code should look something like this:

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

# * Look closely at your results, and make sure you understand why each 
#       line evaluates to True or False.

# * Create at least ten tests. Have at least five tests evaluate to 
#       True and another five tests evaluate to False.

first_name = 'Kacper'
print("\nIs first_name == 'kacper'? I predict False.")
print(first_name == 'kacper')

print("\nIs first_name == 'kacper'? I predict True.")
print(first_name.lower() == 'kacper')

known_languages = ['polish', 'english']

if 'python' in known_languages:
    print("\nCongratulations you finaly know python!")
else:
    print("\nLearn python faster you.")


my_age = 25
cat_age = 1
print("\nAm I younger than my cat? I predict False.")
print(my_age<cat_age)

print("\nAm I older than my cat? I predict True.")
print(my_age>cat_age)

my_friends = ['Vacool', 'Kaczor', 'Mc']
print("\nIs Kaczor my friend? I predict True.")
print('Kaczor' in my_friends)
print("\nIs Targen my friend? I predict False.")
print('Targen' in my_friends)

number1 = 12
number2 = 21
print("\nIs any number over or equal to 20? I predict True.")
print(number1 >= 20 or number2 >= 20)
number2 = 19

print("\nIs any number over or equal to 20? I predict False.")
print(number1 >= 20 or number2 >= 20)

