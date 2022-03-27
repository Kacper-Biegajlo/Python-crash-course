## 9-11. Imported Admin: 
# 
# Start with your work from Exercise 9-8 (page 173). 
# 
# Store the classes User, Privileges, and Admin in one module. 
# 
# Create a separate file, make an Admin instance, and call show_privileges() to 
#   show that everything is working correctly.

from users_modules import Privileges, Admin

# TESTING
kaczor_user = Admin('Dariusz', 'Kaczyński', 'Kaczor', '69')
kaczor_user.privileges.show_privileges()