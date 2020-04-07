#! /usr/bin/python3

"""
Configuration file.
Please open with a plain text editor.
"""

scale = 1.5
carddims = (int(74*scale), int(104*scale))

back_filename = 'cards/429px-Magic_card_back.bmp'

grayback_filename = 'cards/429px-Magic_card_back_gray.bmp'

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)

lands = {
'lands/plains.bmp': 0,
'lands/island.bmp': 0,
'lands/swamp.bmp': 31,
'lands/mountain.bmp': 0,
'lands/forest.bmp': 0,
}

decklist_dir = 'yawgmoth_edh/'

decklist_filename = 'yawgmoth_edh/ytp_edh.txt'
