#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 00:20:02 2020

@author: twore
"""

import pygame
import random
import sys 

x = 500
y = 500
Colourmap=[
[0,	0,0],
[0,0,128],
[0,0,255],
[128,0,0],
[128,0,128],
[128,0,255],
[255,0,	0],
[255,0,128],
[255,0,255],
[0,128,0],
[0,128,128],
[0,128,255],
[128,128,0],
[128,128,128],
[128,128,255],
[255,128,0],
[255,128,128],
[255,128,255],
[0,255,0],
[0,255,	128],
[0,255,255],
[128,255,0],
[128,255,128],
[128,255,255],
[255,255,0],
[255,255,128],
[255,255,255]
]
pygame.init()
screen = pygame.display.set_mode([x,y])
clock = pygame.time.Clock()
screen.fill((0,0,0))
cm_index=0
x=0;y=0
stil = pygame.font.SysFont("Tahoma",25,False,False)
#load tilemap
tilemap=pygame.image.load("/home/twore/Schreibtisch/spyder/pygame/tilemap2.png").convert()
#load tilesettings
tile1=pygame.image.load("test_2.png").convert()

#function plot tile from tilemap @ tx,ty to screen x,y
def tiletest(x,y,tx,ty,tilemap,tile1) :
    gg=tilemap.copy()
    gg.blit(tilemap, (tx, ty))
    tile1.blit(gg,[0,0])
    screen.blit(tile1,[x,y])
    return 1
    
#main loop work till ESC is pressed
done = False
while not done:
    for event in pygame.event.get():
         speed=0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    keys=pygame.key.get_pressed()
    if keys[pygame.K_DOWN]:
        speed=-1
    if keys[pygame.K_UP]:
        speed=1
    x=x+speed
    if x<-160:
        x=-160
    if keys[pygame.K_ESCAPE]:
        done = True
    print(x)
    print(done)
    ################################
    # mein programmcode            #
    ################################
    
    #pygame.draw.rect(screen,Colourmap[cm_index],[20,20,30,30])
    cm_index+=1
    if cm_index>26:
        cm_index=0
    #plot line
    tx=x
    ty=y
    tiletest(x+128,y,tx,ty,tilemap,tile1) 
    pygame.display.flip()
    clock.tick(30)
pygame.quit()