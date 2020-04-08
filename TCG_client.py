#! /usr/bin/python3

import pygame
import sys
from data.network import Network
from data.TCG_classes import *
from TCG_config import *

width = 1600
height = 800
win = pygame.display.set_mode((width, height))

pygame.display.set_caption("Trading Card Game")

def redrawWindow(win,players,d):
    win.fill((255,255,255))
    img = pygame.image.load(d.looking).convert_alpha()
    img = pygame.transform.scale(img,(carddims[0]*2,carddims[1]*2))
    win.blit(img,(width-carddims[0]*2, height//3))
    for player in players:
        player.print(win)
    pygame.display.update()

def main():
    run = True
    look = back_filename

    n = Network()
    p = n.getP()
    clock = pygame.time.Clock()

    d = Deck(p)
    d.load()

    while run:
        clock.tick(60)
        mouse_x, mouse_y =  pygame.mouse.get_pos()

        players = n.send(p)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

            d.drag(event)
            d.standby(event)
            d.manage(event, mouse_x, mouse_y)

            for cntr in p.counterlist:
                cntr.drag(event)
                cntr.standby(event)
                cntr.transform()
                cntr.put_on_deck(event)
  
            for crd in p.cardsinplay:
                crd.drag(event)
                crd.standby(event)
                crd.put_on_deck(event,d)
                crd.transform()
                crd.look(d)

        redrawWindow(win, players, d)

if __name__ == "__main__":
    main()
