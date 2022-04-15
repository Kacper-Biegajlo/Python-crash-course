"""Class to make a simple restaurant with few methods."""

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
        """Increment the number of customers who have been served."""
        self.today_number_served = today_number
        self.number_served += today_number
        print(f"With {self.today_number_served} customers served\
 today, we served {self.number_served} customers in total. ")