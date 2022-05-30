### Changing, Adding, and Removing Elements ###


# Modifying Elements in a List          

motorcycles = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles)

motorcycles[0] = 'ducati'         # changing first value in the list
print(motorcycles)


## Adding Elements to a List ##

# Appending Elements to the End of a List

motorcycles.append('ducati')      # .append adds new value at the end of existing list
print(motorcycles)       

motorcycles = []                  # example of an empty list being build
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# Inserting Elements into a List

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')      # .insert adds new value to the list at the specific postion
print(motorcycles)


## Removing Elements from a List ##

# Removing an Item Using the del Statement

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0] # del removes value from the list at specific position
print(motorcycles)

del motorcycles[1]
print(motorcycles)

# Removing an Item Using the pop() Method

motorcycles = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles)
popped_motorcycle = motorcycles.pop() # .pop() removes last item from the list and saves it
print(motorcycles)
print(popped_motorcycle)   

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop() # example of .pop() usage
print(f"The last motorcycle I owned was a {last_owned.title()}.")

# Popping Items from any Position in a List

first_owned = motorcycles.pop(0) # you can use .pop to choose specific element from the list by using it position  in ()
print(f"The first motorcycle I owned was a {first_owned.title()}.")

# Removing an Item by Value

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati') # .remove lets you remove elemtn from by list by value and not position
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive) 
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.") # you can use removed value from the list as it was assigned to variable




