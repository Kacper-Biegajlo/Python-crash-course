## 9-6. Ice Cream Stand: 
# 
# An ice cream stand is a specific kind of restaurant. 
# 
# Write a class called IceCreamStand that inherits from the Restaurant 
#   class you wrote in Exercise 9-1 (page 162) or Exercise 9-4 (page 167). 
# 
# Either version of the class will work; just pick the one you like better. 
# 
# Add an attribute called flavors that stores a list of ice cream flavors. 
# 
# Write a method that displays these flavors. 
# 
# Create an instance of IceCreamStand, and call this method.

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

class IceCreamStand(Restaurant):
    """Subclass of Restaurant class."""
    
    def __init__(self, restaurant_name, *flavors):
        """Inheriting attributes from parent class."""
        super().__init__(restaurant_name, cuisine_type='ice creams')
        self.flavors = flavors
    
    def add_flavors(self):
        """Prints avaiable flavors."""
        Ice_flavors = []
        print("Ice cream flavors:")
        for flavor in self.flavors:
            Ice_flavors.append(flavor)
        print(Ice_flavors)
#       print(self.flavors)     this could also work

# TESTING IF WORKS 

u_kaczora = IceCreamStand('U Kaczora', 'chocolate', 'strawberry', 'lemon')
u_kaczora.describe_restaurant()
u_kaczora.add_flavors()

u_vacoola = IceCreamStand('U Vacoola', 'potato', 'tomato', 'lemon')
u_vacoola.describe_restaurant()
u_vacoola.add_flavors()

# making sure
u_kaczora.add_flavors()

# Ok so the issue is that you can either make a list or just print self.flavors.
# Because there is a word list in exercise I made a function that moves all 
#   the flavors from sel.flavors into list called Ice_flavors ??????