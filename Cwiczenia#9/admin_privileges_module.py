"""Classes for privileges and admin"""

from user_module import User

class Privileges:
    """Class for describing privileges."""

    def __init__(self, *privileges):
        """Stores a list of privileges."""
        self.privileges = privileges

    def show_privileges(self):
        """Prints list of privilages."""
        print(f"List of current privilages:")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(User):
    """Special "admin" subclass of user."""
    def __init__(self, first_name, last_name, nickname, user_age):   
        
        """Inheriting attributes from parent class."""
        super().__init__(first_name, last_name, nickname, user_age)
        
        self.privileges = Privileges('can ban users', 'can edit posts'\
 , 'is your master', 'can call you a pleb')