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
make_album('Loveworld singers', 'Praise night 15', 20)

