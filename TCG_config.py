#! /usr/bin/python3

"""
Configuration file.
Please open with a plain text editor.
"""

server_ip = "192.168.0.5"

# control the size of the cards
scale = 1.5
carddims = (int(74*scale), int(104*scale))

# the image for the back of the cards always leave the "data/cards/" string
back_filename = 'data/cards/429px-Magic_card_back.bmp'

# the image for the token cards
token_filename = 'data/cards/429px-Magic_card_back_gray.bmp'

# the directory to the deck to be loaded
decklist_dir = 'vannifar_edh/'

# the file that contains the list of image files
decklist_filename = 'vannifar_edh/psv_edh.txt'

# the cards that are going to be replicated
repeat = {
'data/cards/plains.bmp': 0,
'data/cards/island.bmp': 13,
'data/cards/swamp.bmp': 0,
'data/cards/mountain.bmp': 0,
'data/cards/forest.bmp': 18,
}

# color definitions for counters
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)
