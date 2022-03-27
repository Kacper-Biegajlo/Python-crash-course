## 9-5. Login Attempts: 
# 
# Add an attribute called login_attempts to your User class from 
#   Exercise 9-3 (page 162). 
# 
# Write a method called increment_login_attempts() that increments the value 
#   of login_attempts by 1. 
# 
# Write another method called reset_login_attempts() that resets the value 
#   of login_attempts to 0.
# 
# Make an instance of the User class and call increment_login_attempts() 
#   several times. 
# 
# Print the value of login_attempts to make sure it was incremented properly, 
#   and then call reset_login_attempts(). 
# 
# Print login_attempts again to make sure it was reset to 0.

class User:
    """Short class of simple user."""

    def __init__(self, first_name, last_name, nickname, user_age):
        """Initialize information about user"""
        self.full_name = f"{first_name} {last_name}"
        self.first_name = first_name
        self.last_name = last_name
        self.nickname = nickname
        self.user_age = user_age
        self.login_attempts = 0

    def describe_user(self):
        """prints a summary of the user’s information."""
        current_user = {
            "first name": self.first_name, 
            "second name": self.last_name, 
            "nickname": self.nickname,
            "user age": self.user_age
        }
        print(current_user)

    def greet_user(self):
        """prints a personalized greeting to the user."""
        print(f"{self.full_name} / {self.nickname} hello and welcome!\n")

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f"{self.nickname} attempted to log in.")
        print(f"{self.nickname} attempted to log in {self.login_attempts} times\
 so far.\n")

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f"Login attempts for {self.nickname} were resseted.\n")

niebieski_user = User('Kacper', 'Biegajło', 'Niebieski', '25')
niebieski_user.describe_user()
niebieski_user.greet_user()

niebieski_user.increment_login_attempts()
niebieski_user.increment_login_attempts()
niebieski_user.increment_login_attempts()
niebieski_user.reset_login_attempts()

print(niebieski_user.login_attempts)
