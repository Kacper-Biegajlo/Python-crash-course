## 6-6. Polling: 
# Use the code in favorite_languages.py (page 97).

# * Make a list of people who should take the favorite languages poll. 
#   Include some names that are already in the dictionary and some that are not.

# * Loop through the list of people who should take the poll. 
# If they have already taken the poll, print a message thanking them for 
#    responding. 
# If they have not yet taken the poll, print a message
#    inviting them to take the poll.

favorite_languages = {
       'jen': 'python',
       'sarah': 'c',
       'edward': 'ruby',
       'phil': 'python',
       }

poll_members = ['kaczor', 'vacool', 'jen','phil']

for poll_member in poll_members:
    if poll_member in favorite_languages:
        print(f"{poll_member.title()} thank you for joining my poll!")
    if poll_member not in favorite_languages:
        print(f"{poll_member.title()} why didn't you join my poll? Sadge.")