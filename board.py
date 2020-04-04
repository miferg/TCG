#! /usr/bin/python3

import pygame
import sys
from network import Network
from player import Player
from cards import *


width = 1000
height = 800
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("TCL Board")
scale = 2
card_dims = (int(74*scale), int(104*scale))

back_filename = 'cards/429px-Magic_card_back.bmp'
back = pygame.image.load(back_filename).convert_alpha()
back = pygame.transform.scale(back,card_dims)

grayback_filename = 'cards/429px-Magic_card_back_gray.bmp'
grayback = pygame.image.load(grayback_filename).convert_alpha()
grayback = pygame.transform.scale(grayback,card_dims)

################################################################################
#yawgmoth EDH
lands = []
for i in range(0,31):
    lands.append('swamp.bmp')

handle = open('yawgmoth_edh/ytp_edh.txt','r')
decklist = handle.read().split('\n')[:-1]
handle.close()

deckdir = 'yawgmoth_edh/'
################################################################################

def redrawWindow(win,player, player2):
    win.fill((255,255,255))
    player.draw(win)
    player2.draw(win)
    pygame.display.update()


def main():
    run = True
    #n = Network()
    #p = n.getP()
    clock = pygame.time.Clock()

    cardsindeck = []

    for i in lands:
        front = pygame.image.load('lands/'+i).convert_alpha()
        front = pygame.transform.scale(front,card_dims)
        cardsindeck.append(Card(0, 0, card_dims[0], card_dims[1], (20,20,20), back, front))

    for i in decklist:
        front = pygame.image.load(deckdir+i).convert_alpha()
        front = pygame.transform.scale(front,card_dims)
        cardsindeck.append(Card(0, 0, card_dims[0], card_dims[1], (20,20,20), back, front))

    d = Deck(0, 0, card_dims[0], card_dims[1], (20,20,20), back, cardsindeck)

    decksinplay = [d]

    cardsinplay = []

    while run:
        clock.tick(60)
        #p2 = n.send(p)

        mouse_x, mouse_y =  pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

            for crd in cardsinplay:
                crd.drag(event)
                crd.standby(event)
                crd.put_on_deck(event, cardsinplay, decksinplay)

            for deck in decksinplay:
                deck.drag(event)
                deck.standby(event)

        win.fill((255,255,255))

        for deck in decksinplay:
            deck.manage()
            deck.print(win)
            drawed = deck.draw()
            if drawed:
                drawed.x = mouse_x
                drawed.y = mouse_y
                drawed.update()
                cardsinplay.append(drawed)
            newtoken = deck.token(mouse_x, mouse_y, grayback)
            if newtoken:
                cardsinplay.append(newtoken)

        #if len(cardsinplay) > 0:
        for crd in cardsinplay:
            crd.transform()
            crd.print(win)

        #p.move()
        #redrawWindow(win, p, p2)
        pygame.display.update()

main()
