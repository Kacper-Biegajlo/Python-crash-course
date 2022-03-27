## 9-10. Imported Restaurant: 
# 
# Using your latest Restaurant class, store it in a module. 
# 
# Make a separate file that imports Restaurant. 
# 
# Make a Restaurant instance, and call one of Restaurant’s methods to show t
#   hat the import statement is working properly.

from restaurant_module import Restaurant

# testing the instance
polish_restaurant = Restaurant('Na Grubo', 'pierogi')

polish_restaurant.set_number_served(6969)

polish_restaurant.increment_number_served(42)