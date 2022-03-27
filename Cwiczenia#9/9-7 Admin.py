## 9-7. Admin: 
# 
# An administrator is a special kind of user. 
# 
# Write a class called Admin that inherits from the User class you wrote in 
#   Exercise 9-3 (page 162) or Exercise 9-5 (page 167). 
# 
# Add an attribute, privileges, that stores a list of strings like 
#   "can add post", "can delete post", "can ban user", and so on. 
# 
# Write a method called show_privileges() that lists the administrator’s set 
#   of privileges. 
# 
# Create an instance of Admin, and call your method.

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

class Admin(User):
    """Special "admin" subclass of user."""
    def __init__(self, first_name, last_name, nickname, user_age, *privileges):   
        
        """Inheriting attributes from parent class."""
        super().__init__(first_name, last_name, nickname, user_age)
        
        self.privileges = privileges

    def show_privileges(self):
        """Prints list of privilages for that subclass."""
        print(f"List of current privilages for {self.nickname.title()}:")
        for privilege in self.privileges:
            print(f"- {privilege}")

# TESTING

niebieski_user = Admin('Kacper', 'Biegajło', 'Niebieski', '25',\
 'can ban users', 'can edit posts', 'is your master', 'can call you a pleb')
niebieski_user.describe_user()
niebieski_user.greet_user()
niebieski_user.show_privileges()