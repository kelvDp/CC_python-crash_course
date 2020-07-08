def make_album(name, title, songs=None):
    album = {"artist_name": name, "album_title": title}
    if songs:
        album["songs"] = songs
    return album

while True:
    artist = input("Please enter an artist (enter q to stop) :")
    if artist == "q":
        break
    album = input("Please enter an album name :")
    print(make_album(artist,album))

