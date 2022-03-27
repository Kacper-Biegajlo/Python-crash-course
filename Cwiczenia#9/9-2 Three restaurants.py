## 9-2. Three Restaurants: 
# 
# Start with your class from Exercise 9-1. 
# 
# Create three different instances from the class, and call 
#   describe_restaurant() for each instance.

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

ramen_restaurant = Restaurant('Uki Uki', 'ramen')
fastfood_restaurant = Restaurant('Burger King', 'burgers')
kebab_restaurant = Restaurant('Chata Wariata', 'kebabs')

ramen_restaurant.describe_restaurant()
fastfood_restaurant.describe_restaurant()
kebab_restaurant.describe_restaurant()