## 5-9. No Users: 
#  Add an if test to hello_admin.py to make sure the list of users is not empty.

# * If the list is empty, print the message We need to find some users!

# * Remove all of the usernames from your list,
#    and make sure the correct message is printed.

users = ['admin', 'niebieski', 'kaczor', 'mc', 'vacool']
if users == []:
    print("We need to find some users!")
else:
    for user in users:
        if user == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {user.title()}, thank you for logging in again.") 

users = []
if users == []:
    print("We need to find some users!")
else:
    for user in users:
        if user == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {user.title()}, thank you for logging in again.") 