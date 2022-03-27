## 9-1. Restaurant: 
# 
# Make a class called Restaurant. 
# 
# The __init__() method for Restaurant should store two attributes: 
# a restaurant_name and a cuisine_type. 
# 
# Make a method called describe_restaurant() that prints these two 
#   pieces of information, and a method called open_restaurant() that prints 
#       a message indicating that the restaurant is open.
# 
# Make an instance called restaurant from your class. 
# 
# Print the two attributes individually, and then call both methods.

class Restaurant:
    """Short class of a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Present description of the restaurant with inserted info."""
        print(f"{self.restaurant_name} offers {self.cuisine_type}.")

    def open_restaurant(self):
        """Show short message that informs about restaurant opening"""
        print(f"{self.restaurant_name} is currently open!")

polish_restaurant = Restaurant('Na Grubo', 'pierogi')

print(polish_restaurant.restaurant_name)
print(polish_restaurant.cuisine_type)

polish_restaurant.describe_restaurant()
polish_restaurant.open_restaurant()





