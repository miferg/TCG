#! /usr/bin/python3

"""
classes for the TCL board

"""

import pygame
import random

##########################################################################################

class Card():
    def __init__(self, x, y, width, height, color, back, front):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)
        self.vel = 3
        self.offset_x = 0
        self.offset_y = 0
        self.rectangle_draging = False
        self.back = back
        self.front = front
        self.show = back
        self.standingby = False
        self.rback = pygame.transform.rotate(self.back, 270)
        self.rfront = pygame.transform.rotate(self.front, 270)

    def print(self, win):
        pygame.draw.rect(win, self.color, self.rect)
        win.blit(self.show,(self.x, self.y))

    def drag(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:            
                if pygame.rect.Rect(self.x, self.y, self.width, self.height).collidepoint(event.pos):
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

    def put_on_deck(self, event, cardsinplay, decksinplay):
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                for d in decksinplay:
                    selfrect = pygame.rect.Rect(self.x, self.y, self.width, self.height)
                    drect = pygame.rect.Rect(d.rect)
                    if selfrect.colliderect(drect):
                        cardsinplay.remove(self)
                        d.cardlist.append(self)
                        
    def standby(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                if pygame.rect.Rect(self.x, self.y, self.width, self.height).collidepoint(event.pos):
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
                if self.show == self.back:
                    self.show = self.rback
                elif self.show == self.rback:
                    self.show = self.back
                elif self.show == self.front:
                    self.show = self.rfront
                elif self.show == self.rfront:
                    self.show = self.front
                self.standingby = False

    def update(self):
        self.x = max(0,self.x)
        self.y = max(0,self.y)
        self.rect = (self.x, self.y, self.width, self.height)

################################################################################

class Deck():

    def __init__(self, x, y, width, height, color, back, cardlist):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)
        self.vel = 3
        self.offset_x = 0
        self.offset_y = 0
        self.rectangle_draging = False
        self.back = back
        self.show = back
        self.standingby = False
        self.rback = pygame.transform.rotate(self.back, 270)
        self.cardlist = cardlist

    def print(self, win):
        pygame.draw.rect(win, self.color, self.rect)
        win.blit(self.show,(self.x, self.y))

    def drag(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:            
                if pygame.rect.Rect(self.x, self.y, self.width, self.height).collidepoint(event.pos):
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
                if pygame.rect.Rect(self.x, self.y, self.width, self.height).collidepoint(event.pos):
                    self.standingby = True

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 3:
                self.standingby = False

    def draw(self):
        if self.standingby:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_d]:
                self.standingby = False
                if len(self.cardlist) > 0:
                    return self.cardlist.pop()

    def token(self, x, y, grayback):
        if self.standingby:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_t]:
                self.standingby = False
                return Token(x, y, self.width, self.height, (20,20,20), grayback)

    def manage(self):
        if self.standingby:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_s]:			#s: shuffle
                self.standingby = False
                if len(self.cardlist) > 0:
                    random.shuffle(self.cardlist)
            elif keys[pygame.K_b]:			#b: send to back
                self.standingby = False
                if len(self.cardlist) > 0:
                    self.cardlist = [self.cardlist[-1]] + self.cardlist[:-1]

    def update(self):
        self.x = max(0,self.x)
        self.y = max(0,self.y)
        self.rect = (self.x, self.y, self.width, self.height)

################################################################################

class Token():
    def __init__(self, x, y, width, height, color, back):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)
        self.vel = 3
        self.offset_x = 0
        self.offset_y = 0
        self.rectangle_draging = False
        self.back = back
        self.show = back
        self.standingby = False
        self.rback = pygame.transform.rotate(self.back, 270)

    def print(self, win):
        pygame.draw.rect(win, self.color, self.rect)
        win.blit(self.show,(self.x, self.y))

    def drag(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:            
                if pygame.rect.Rect(self.x, self.y, self.width, self.height).collidepoint(event.pos):
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

    def put_on_deck(self, event, cardsinplay, decksinplay):
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                for d in decksinplay:
                    selfrect = pygame.rect.Rect(self.x, self.y, self.width, self.height)
                    drect = pygame.rect.Rect(d.rect)
                    if selfrect.colliderect(drect):
                        cardsinplay.remove(self)

    def standby(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                if pygame.rect.Rect(self.x, self.y, self.width, self.height).collidepoint(event.pos):
                    self.standingby = True

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 3:
                self.standingby = False

    def transform(self):
        if self.standingby:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_t]:			#t: tap
                if self.show == self.back:
                    self.show = self.rback
                elif self.show == self.rback:
                    self.show = self.back
                self.standingby = False

    def update(self):
        self.x = max(0,self.x)
        self.y = max(0,self.y)
        self.rect = (self.x, self.y, self.width, self.height)

################################################################################
