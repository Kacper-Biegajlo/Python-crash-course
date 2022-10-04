## 6-9. Favorite Places: 
#
# Make a dictionary called favorite_places. 
# Think of three names to use as keys in the dictionary, 
#   and store one to three favorite places for each person. 
# To make this exercise a bit more interesting, ask some friends to name 
#   a few of their favorite places. 
# Loop through the dictionary, 
#   and print each person’s name and their favorite places.

fav_places = {
    'Kaczor': ['Sławacinek', 'bed'],
    'Vacool': ['Gym','Bed'],
    'Mc': ['Taxi', 'Budka z kebabem'],
}

for chad, places in fav_places.items():
    print(f"{chad}'s favorite places are:")
    for place in places:
        print(f"- {place.title()}")