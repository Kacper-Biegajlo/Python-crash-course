## 9-4. Number Served: 
# 
# Start with your program from Exercise 9-1 (page 162). 
# 
# Add an attribute called number_served with a default value of 0. 
# 
# Create an instance called restaurant from this class. 
# 
# Print the number of customers the restaurant has served, and then change 
#   this value and print it again.
# 
# - Add a method called set_number_served() that lets you set the number 
#   of customers that have been served. 
# Call this method with a new number and print the value again.
# 
# - Add a method called increment_number_served() that lets you 
#   increment the number of customers who’ve been served. 
# Call this method with any number you like that could represent how many 
#   customers were served in, say, a day of business.

class Restaurant:
    """Short class of a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Present description of the restaurant with inserted info."""
        print(f"{self.restaurant_name} offers {self.cuisine_type}.")

    def open_restaurant(self):
        """Show short message that informs about restaurant opening"""
        print(f"{self.restaurant_name} is currently open!")
    
    def set_number_served(self, number):
        """Set the number of customers that have been served."""
        self.number_served = number
        print(f"{self.restaurant_name} served\
 {self.number_served} customers in total.")
    
    def increment_number_served(self, today_number):
        """Increment the number of customers who’ve been served."""
        self.today_number_served = today_number
        self.number_served += today_number
        print(f"With {self.today_number_served} customers served\
 today, we served {self.number_served} customers in total. ")



# testing the instance
polish_restaurant = Restaurant('Na Grubo', 'pierogi')

print(polish_restaurant.restaurant_name)
print(polish_restaurant.cuisine_type)

polish_restaurant.describe_restaurant()
polish_restaurant.open_restaurant()

# testing number of customers served with manual changes
print(polish_restaurant.number_served)
polish_restaurant.number_served = 10
print(polish_restaurant.number_served)

# testing method that sets number of customers served
polish_restaurant.set_number_served(69)

# testing method that increments number of customers served
polish_restaurant.increment_number_served(420)


