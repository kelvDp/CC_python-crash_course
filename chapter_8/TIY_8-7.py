def make_album(name,title,songs=None):
    album = {"artist_name":name,"album_title":title}
    if songs:
        album["songs"]= songs
    return album

album1 = make_album("John","Music")
album2 = make_album("Jane","Classical")
album3 = make_album("Dave","Popping")
# you can also simply print the function since it has a return value
print(album1)
print(album2)
print(album3)
print("\n")

album4 = make_album("Alexi","Sounds",songs=12)
print(album4)