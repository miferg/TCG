# Trading Card Game

A virtual tabletop designed to play TCGs through a network.
Tested in Ubuntu 16.04 and macOS High Sierra.

phyrexian.kavu@gmail.com

## Dependencies:

- python3.6~
- pygame 1.9.6


## Launching the tabletop

To start playing, write down the ip addres of the server in the TCG_config.py,
then launch a server from a terminal with the following command:

python3 TCG_server.py

Then each player must launch the client in their terminals:

python3 TCG_client.py


## Tabletop interface

Functions:

- Hold left-click and move the mouse to drag objects.
  Be careful when placing decks (see below).

Right-click + Key functions (clicks must be hold until the appropiate key is pressed):

- d: Draw a card.
- s: Shuffle the deck.
- u: Put the first card on the top of the deck on the bottom of the deck.
- k: Create a token.
- r: Create a red counter.
- g: Create a green counter.
- b: Create a blue counter.

Right-click over an object + Key functions:

- l: Display a card at the card viewer (look).
- f: Turn a card over (flip).
- t: Rotate a card 90º to the right (tap).
- 1-9: change the value of a token

Players can only manipulate their own objects and cannot see what other players see in 
their card viewer at the right side of the board.

The decks are represented by the card back image and can be dragged. If a deck collides 
with a card on the board, the card is placed at the top of the deck. If tokens and 
counters touch a deck, they are deleted.


## Configuration file

**TCG_config.py**

The only file ment to be modified by the end user. It contains the references that define
the information being processed by the tabletop. It is a python3 file but it is not ment
to be executed. Contents:

- server_ip: the Ipv4 adress of the server.
- scale: the size ratio of the cards, asuming thay have standard dimensions.
- carddims: the final size of the cards, the card viewer will have these dimensions doubled.
- back_filename: the name of the file for the back of the cards.
- token_filename: the name of the image file for tokens.
- decklist_dir: the directory containing the bmp iage files of the deck to load.
- decklist_filename: the name of the file that contains the list of image files.
- repeat: a dictionary that contains the names and the number of cards to add replicated.
- color definitions


## Building a deck

You must be advised that the card images will be forced to the standard cards size ratio and all
images must be in bmp format.

Select an image for the back of the cards and for the token objects and save them in the "cards"
subdirectory of the "data" folder (TCG/data/cards/). Some games have repetitive cards such as lands or energies, save only one of each type of them in the cards directory. Create a new directory in the
TCG directory and store there the bmp image files for the remainder of the deck. Make a list file of
the deck image files and save it in the deck directory (in unix is as simple as "ls *.bmp > list.txt").
Edit the TCG_config.py file accordingly and you are done. Note that all players must have a copy of
the image files in their "data/cards/" and deck directories to be printed on the board.


