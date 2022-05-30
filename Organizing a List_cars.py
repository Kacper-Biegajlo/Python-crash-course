## Organizing a List ##

# Sorting a List Permanently with the sort() Method

cars = ['bmw', 'audi', 'toyota', 'subaru'] 
cars.sort() # .sort() lets you sort list alphabetically 
print(cars)
print("\t")


cars.sort(reverse=True) # that method sorts your list in reverse alphabeticall order
print(cars)
print("\t")

# Sorting a List Temporarily with the sorted() Function

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:") 
print(cars)
print("\nHere is the sorted list:") 
print(sorted(cars)) # sorted() function sorts list temporarly
print("\nHere is the original list again:") 
print(cars)
print("\t")


# Printing a List in Reverse Order

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse() # .reverse() function reverses order of the list
print(cars)
print("\t")

# Finding the Length of a List

cars = ['bmw', 'audi', 'toyota', 'subaru'] 
len(cars) # len() function finds a lenghts of the list

