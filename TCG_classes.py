#! /usr/bin/python3

import pygame
import random
from TCG_config import *

pygame.font.init()

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)

class Player():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = (x,y,carddims[0],carddims[1])
        self.cardsinplay = []
        self.tokenlist = []
        self.counterlist = []
        self.back = back_filename

    def print(self, win):
        back = pygame.image.load(self.back).convert_alpha()
        back = pygame.transform.scale(back,(carddims[0],carddims[1]))
        win.blit(back,(self.x, self.y))
        for crd in self.cardsinplay:
            img = pygame.image.load(crd.show).convert_alpha()
            img = pygame.transform.scale(img,(carddims[0],carddims[1]))
            if crd.tapped:
                img = pygame.transform.rotate(img, 270)
            win.blit(img,(crd.x, crd.y))
        for cntr in self.counterlist:
            pygame.draw.rect(win, cntr.color, cntr.rect)
            textsurface = pygame.font.Font(None,cntr.font).render(str(cntr.counter), False, white)
            win.blit(textsurface,(cntr.x+cntr.size//4,cntr.y+cntr.size//16))

################################################################################

class Counter():
    def __init__(self, x, y, color, player):
        self.x = x
        self.y = y
        self.size = carddims[0]//3
        self.color = color
        self.rect = (x,y,self.size,self.size)
        self.offset_x = 0
        self.offset_y = 0
        self.rectangle_draging = False
        self.standingby = False
        self.counter = 1
        self.font = (carddims[0] // 2)
        self.player = player

    def update(self):
        self.rect = (self.x, self.y,self.size,self.size)

    def drag(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:            
                if pygame.rect.Rect(self.x, self.y,self.size,self.size).collidepoint(event.pos):
                    self.rectangle_draging = True
                    mouse_x, mouse_y = event.pos
                    self.offset_x = self.x - mouse_x
                    self.offset_y = self.y - mouse_y

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.rectangle_draging = False

        elif event.type == pygame.MOUSEMOTION:
            if self.rectangle_draging:
                mouse_x, mouse_y = event.pos
                self.x = mouse_x + self.offset_x
                self.y = mouse_y + self.offset_y
        self.update()

    def put_on_deck(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                selfrect = pygame.rect.Rect(self.x, self.y,self.size,self.size)
                drect = pygame.rect.Rect(self.player.rect)
                if selfrect.colliderect(drect):
                    self.player.counterlist.remove(self)

    def standby(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                if pygame.rect.Rect(self.x, self.y,self.size,self.size).collidepoint(event.pos):
                    self.standingby = True

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 3:
                self.standingby = False

    def transform(self):
        if self.standingby:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_1]:			#1: counter changes to 1
                self.counter = 1
                self.standingby = False
            elif keys[pygame.K_2]:			#2: counter changes to 2
                self.counter = 2
                self.standingby = False
            elif keys[pygame.K_3]:			#3: counter changes to 3
                self.counter = 3
                self.standingby = False
            elif keys[pygame.K_4]:			#4: counter changes to 4
                self.counter = 4
                self.standingby = False
            elif keys[pygame.K_5]:			#5: counter changes to 5
                self.counter = 5
                self.standingby = False
            elif keys[pygame.K_6]:			#6: counter changes to 6
                self.counter = 6
                self.standingby = False
            elif keys[pygame.K_7]:			#7: counter changes to 7
                self.counter = 7
                self.standingby = False
            elif keys[pygame.K_8]:			#8: counter changes to 8
                self.counter = 8
                self.standingby = False
            elif keys[pygame.K_9]:			#9: counter changes to 9
                self.counter = 9
                self.standingby = False
        self.update()

################################################################################

class Card():
    def __init__(self, x, y, back_filename, front_filename, player):
        self.x = x
        self.y = y
        self.rect = (x,y,carddims[0],carddims[1])
        self.offset_x = 0
        self.offset_y = 0
        self.rectangle_draging = False
        self.back = back_filename
        self.front = front_filename
        self.show = self.back
        self.standingby = False
        self.tapped = False
        self.player = player

    def update(self):
        self.rect = (self.x,self.y,carddims[0],carddims[1])

    def drag(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:            
                if pygame.rect.Rect(self.x, self.y,carddims[0],carddims[1]).collidepoint(event.pos):
                    self.rectangle_draging = True
                    mouse_x, mouse_y = event.pos
                    self.offset_x = self.x - mouse_x
                    self.offset_y = self.y - mouse_y

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.rectangle_draging = False

        elif event.type == pygame.MOUSEMOTION:
            if self.rectangle_draging:
                mouse_x, mouse_y = event.pos
                self.x = mouse_x + self.offset_x
                self.y = mouse_y + self.offset_y
        self.update()

    def standby(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                if pygame.rect.Rect(self.x, self.y,carddims[0],carddims[1]).collidepoint(event.pos):
                    self.standingby = True

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 3:
                self.standingby = False

    def transform(self):
        if self.standingby:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_f]:			#f: flip
                if self.show == self.back:
                    self.show = self.front
                elif self.show == self.front:
                    self.show = self.back
                self.standingby = False
            elif keys[pygame.K_t]:			#t: tap
                if self.tapped:
                    self.tapped = False
                else:
                    self.tapped = True
                self.standingby = False
        self.update()

    def look(self, deck):
        if self.standingby:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_l]:			#l: look
                self.standingby = False
                deck.looking = self.front

    def put_on_deck(self, event, deck):
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self_rect = pygame.rect.Rect(self.x, self.y, carddims[0], carddims[1])
                deck_rect = pygame.rect.Rect(self.player.rect)
                if self_rect.colliderect(deck_rect):
                    self.player.cardsinplay.remove(self)
                    deck.cardlist.append(self)

################################################################################

class Token(Card):
    def __init__(self, x, y, back_filename, player):
        self.x = x
        self.y = y
        self.rect = (x,y,carddims[0],carddims[1])
        self.offset_x = 0
        self.offset_y = 0
        self.rectangle_draging = False
        self.back = grayback_filename
        self.show = self.back
        self.standingby = False
        self.tapped = False
        self.player = player

    def transform(self):
        if self.standingby:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_t]:			#t: tap
                if self.tapped:
                    self.tapped = False
                else:
                    self.tapped = True
                self.standingby = False
        self.update()

    def put_on_deck(self, event, deck):
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self_rect = pygame.rect.Rect(self.x, self.y, carddims[0], carddims[1])
                deck_rect = pygame.rect.Rect(self.player.rect)
                if self_rect.colliderect(deck_rect):
                    self.player.cardsinplay.remove(self)

################################################################################

class Deck():
    def __init__(self, player):
        self.player = player
        self.cardlist = []
        self.deckfile = decklist_filename
        self.lands = lands
        self.back = back_filename
        self.standingby = False
        self.rectangle_draging = False
        self.looking = back_filename

    def update(self):
        self.player.rect = (self.player.x, self.player.y, carddims[0], carddims[1])

    def load(self):
        handle = open(self.deckfile,'r')
        decklist = handle.read().split('\n')[:-1]
        handle.close()
        for key in list(self.lands.keys()):
            for i in range(0,lands[key]):
                self.cardlist.append(Card(0,0,self.back,key,self.player))
        for crd in decklist:
            self.cardlist.append(Card(0,0,self.back,decklist_dir+crd,self.player))

    def standby(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                self.standingby = True

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 3:
                self.standingby = False

    def manage(self, event, mouse_x, mouse_y):
        if self.standingby:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_s]:			#s: shuffle
                self.standingby = False
                if len(self.cardlist) > 0:
                    random.shuffle(self.cardlist)
            elif keys[pygame.K_u]:			#b: send under
                self.standingby = False
                if len(self.cardlist) > 0:
                    self.cardlist = [self.cardlist[-1]] + self.cardlist[:-1]
            elif keys[pygame.K_r]:			#r: create a red counter
                self.standingby = False
                self.player.counterlist.append(Counter(mouse_x, mouse_y, red, self.player))
            elif keys[pygame.K_g]:			#g: create a green counter
                self.standingby = False
                self.player.counterlist.append(Counter(mouse_x, mouse_y, green, self.player))
            elif keys[pygame.K_b]:			#b: create a blue counter
                self.standingby = False
                self.player.counterlist.append(Counter(mouse_x, mouse_y, blue, self.player))
            elif keys[pygame.K_d]:			#d: draw card
                self.standingby = False
                if len(self.cardlist) > 0:
                    drawed = self.cardlist.pop()
                    drawed.x = mouse_x
                    drawed.y = mouse_y
                    drawed.update()
                    self.player.cardsinplay.append(drawed)
            elif keys[pygame.K_k]:			#k: create a token
                self.standingby = False
                token = Token(mouse_x, mouse_y, back_filename, self.player)
                self.player.cardsinplay.append(token)

    def drag(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:            
                if pygame.rect.Rect(self.player.rect).collidepoint(event.pos):
                    self.rectangle_draging = True
                    mouse_x, mouse_y = event.pos
                    self.offset_x = self.player.x - mouse_x
                    self.offset_y = self.player.y - mouse_y

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.rectangle_draging = False

        elif event.type == pygame.MOUSEMOTION:
            if self.rectangle_draging:
                mouse_x, mouse_y = event.pos
                self.player.x = mouse_x + self.offset_x
                self.player.y = mouse_y + self.offset_y
        self.update()

################################################################################

