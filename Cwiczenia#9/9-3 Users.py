##  9-3. Users: 
# 
# Make a class called User. 
# 
# Create two attributes called first_name and last_name, and then create 
#   several other attributes that are typically stored in a user profile. 
# 
# Make a method called describe_user() that prints a summary of the 
#   user’s information. 
# 
# Make another method called greet_user() that prints a personalized 
#   greeting to the user.
# 
# Create several instances representing different users, and call both 
#   methods for each user

class User:
    """Short class of simple user."""

    def __init__(self, first_name, last_name, nickname, user_age):
        """Initialize information about user"""
        self.full_name = f"{first_name} {last_name}"
        self.first_name = first_name
        self.last_name = last_name
        self.nickname = nickname
        self.user_age = user_age

    def describe_user(self):
        """prints a summary of the user’s information."""
        self.current_user = {
            "first name": self.first_name, 
            "second name": self.last_name, 
            "nickname": self.nickname,
            "user age": self.user_age
        }
        print(self.current_user)

    def greet_user(self):
        """prints a personalized greeting to the user."""
        print(f"{self.full_name} / {self.nickname} hello and welcome!\n")

niebieski_user = User('Kacper', 'Biegajło', 'Niebieski', '25')
niebieski_user.describe_user()
niebieski_user.greet_user()

kaczor_user = User('Dariusz', 'Kaczyński', 'Kaczor', '69')
kaczor_user.describe_user()
kaczor_user.greet_user()

vacool_user = User('Grzegorz', 'Wakuluk', 'Vacool', '420')
vacool_user.describe_user()
vacool_user.greet_user()

niebieski_user.describe_user()

