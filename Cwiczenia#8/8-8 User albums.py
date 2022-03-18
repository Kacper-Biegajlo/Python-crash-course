## 8-8. User Albums: 
# 
# Start with your program from Exercise 8-7. 
# 
# Write a while loop that allows users to enter an album’s artist and title. 
# 
# Once you have that information, call make_album() with the user’s input and 
#   print the dictionary that’s created. 
# 
# Be sure to include a quit value in the while loop.

def make_album(artist_name, album_name, songs_number=None):
    """Return a dictionary with information about music album."""
    album = {'Artist name': artist_name, 'Album name': album_name, 'Number of\
 songs': songs_number}
    if songs_number:
        album['Number of songs'] = songs_number
    return album

while True:
    print("\nPlease enter album information:")
    print("(enter 'q' at any time to quit)")
    art_name = input("Artist name: ")
    if art_name == 'q':
        break

    alb_name = input("Album name: ")
    if alb_name == 'q':
        break

    song_nbmr = input("Number of songs: ")
    if alb_name == 'q':
        break
    
    custom_input_album = make_album(art_name, alb_name, song_nbmr)
    print(custom_input_album)