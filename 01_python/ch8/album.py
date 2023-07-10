'''
Author: Alphonse Brandon
Date Created: 10-07-2023
Subject: Ch6 - Working python functions
'''

def make_album(name: str, title: str, songs=None) -> None:
    """Describing a music's album"""
    if songs:
        album_info = {
            'Artist' : name,
            'Album' : title,
            'Number of songs' : songs,
        }
    else:
        album_info = {
            'Artist' : name,
            'Album' : title,
        }
    print(album_info)

print("Enter an album's infomation\nEnter 'q' to quit")

while True:
    name = input("Enter the artist name\n")
    if name == 'q':
        break
    title = input("Enter the title of the Album\n")
    if title == 'q':
        break
    print("Album's dictionary:\n")
    make_album(name=name, title=title)

