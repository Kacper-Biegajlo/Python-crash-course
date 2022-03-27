## 9-12. Multiple Modules: 
# 
# Store the User class in one module, and store the Privileges and Admin c
#   lasses in a separate module. 
# 
# In a separate file, create an Admin instance and call show_privileges() to 
#   show that everything is still working correctly.

from admin_privileges_module import Privileges, Admin

# TESTING
vacool_user = Admin('Grzegorz', 'Wakuluk', 'Vacool', '520')
vacool_user.privileges.show_privileges()