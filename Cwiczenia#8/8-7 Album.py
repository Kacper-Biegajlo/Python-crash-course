## 8-7. Album:
# 
# Write a function called make_album() that builds a dictionary 
#   describing a music album. 
# 
# The function should take in an artist name and an album title, and it 
#   should return a dictionary containing these two pieces of information. 
# 
# Use the function to make three dictionaries representing different albums. 
# 
# Print each return value to show that the dictionaries are storing 
#   the album information correctly.
# 
# Use None to add an optional parameter to make_album() that allows you 
#   to store the number of songs on an album. 
# 
# If the calling line includes a value for the number of songs, 
#   add that value to the album’s dictionary. 
# 
# Make at least one new function call that includes the number 
#   of songs on an album.

def make_album(artist_name, album_name, songs_number=None):
    """Return a dictionary with information about music album."""
    album = {'Artist name': artist_name, 'Album name': album_name, 'Number of\
 songs': songs_number}
    if songs_number:
        album['Number of songs'] = songs_number
    return album

album_info_MC = make_album('MC', 'Hotel', '3')
print(album_info_MC)

album_info__Kaczohoe = make_album('Kaczor', 'Best of classic music')
print(album_info__Kaczohoe)

album_info__Vacool = make_album('Vacool', 'Hot Ginger Solos', '69')
print(album_info__Vacool)