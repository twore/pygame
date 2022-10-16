#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 00:20:02 2020

@author: twore
"""
# import librarys for game calculation
import numpy as np
import pygame
import random
import sys 

#create CPC Screen resolution
scale=4
x = 320*scale
y = 200*scale

#create CPC ColourMAP
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
stil = pygame.font.SysFont("Tahoma",25,False,False)
bild0=pygame.image.load("test_0.png").convert()
bild1=pygame.image.load("test_1.png").convert()
bild2=pygame.image.load("test_2.png").convert()
bild3=pygame.image.load("test_3.png").convert()
bild4=pygame.image.load("test_4.png").convert()
bild5=pygame.image.load("test_5.png").convert()
bild6=pygame.image.load("test_6.png").convert()
bild7=pygame.image.load("test_7.png").convert()
bild8=pygame.image.load("test_8.png").convert()
bild9=pygame.image.load("test_9.png").convert()



#create surface
size = width, height = (320, 200)
surface1 = pygame.Surface(size)


sz = surface1.get_size()
sz = [int(sz[0] * scale), int(sz[1] * scale)]

b=[]
b.append(bild1)
b.append(bild2)
b.append(bild3)
b.append(bild4)
b.append(bild5)

#build random map
mapbnm=[]
mapbnmrecal=[]

#init with random stuff
for y_index in range(12*160):
    mapbn=[]
    mapbnrecal=[]
    for x_index in range(20):
                mapbn.append(random.randint(0, 6))
                mapbnrecal.append(0%1)
    mapbnm.append(mapbn)
    mapbnmrecal.append(mapbnrecal)
#connect y
for y_index in range(12*159):
    for x_index in range(20):
        mapbnm[y_index][x_index]+=mapbnm[y_index+1][x_index]
    # mapbn.append(random.randint(0, 2))
  #connect y
for y_index in range(12*160):
    for x_index in range(19):
        mapbnm[y_index][x_index]+=mapbnm[y_index][x_index+1]
     
for y_index in range(12*160):
    for x_index in range(19):
        mapbnm[y_index][x_index]-=3
    # mapbn.append(random.randint(0, 2))for y_index in range(12*160):
for y_index in range(12*160):
    for x_index in range(19):
       if  mapbnm[y_index][x_index]>3:
           mapbnm[y_index][x_index]=3
    # mapbn.append(random.randint(0, 2))
for y_index in range(12*160):
    for x_index in range(19):
        if         mapbnm[y_index][x_index]!=mapbnm[y_index][x_index+1]:
             mapbnm[y_index][x_index]=4

for y_index in range(12*160):
    for x_index in range(19):
        if         (mapbnm[y_index][x_index]==1) and (mapbnm[y_index][x_index+1]==2):
             mapbnm[y_index][x_index]=7
             
for y_index in range(12*160-1):
    for x_index in range(19):
        if         (mapbnm[y_index][x_index]==4) and (mapbnm[y_index][x_index+1]==3):
             mapbnm[y_index][x_index]=8
        if         (mapbnm[y_index][x_index]==3) and (mapbnm[y_index][x_index+1]==4):
             mapbnm[y_index][x_index]=9
        if         (mapbnm[y_index][x_index]==3) and (mapbnm[y_index+1][x_index]==4):
             mapbnm[y_index][x_index]=10
#mapbn=np.array("I")
#    for x_index in range(20):
#        for y_index in range(12*16):
#            mapbn=random.randint(0, 2)
             
for y_index in range(12*160):
    for x_index in range(19):
        print(mapbnm[y_index][x_index], end='')
        
print(8)      
done = False
offs=0
while not done:
    speed=0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    
    keys=pygame.key.get_pressed()
    if keys[pygame.K_DOWN]:
        speed=-1
    if keys[pygame.K_UP]:
        speed=1
                
#            
#        if event.type == pygame.KEYDOWN:
#         if event.key == pygame.K_UP:
#                speed=1
#         if event.key == pygame.K_DOWN:
#                speed=-1
    ################################
    # mein programmcode            #
    ################################
    offs=offs+speed
    offw=offs//16
    offr=offs-offw*16
#    pygame.draw.rect(screen,Colourmap[cm_index],[20,20,30,30])
    cm_index+=1
    if cm_index>26:
        cm_index=0
    #plot line
    for x_index in range(20):
        for y_index in range(13):
            bn=mapbnm[y_index+offw][x_index]
            if bn<=3:
                mapbnmrecal[y_index+offw][x_index]=0
            if bn>3: 
                mapbnmrecal[y_index+offw][x_index]=1
            if bn>5:
                mapbnmrecal[y_index+offw][x_index]=3
            if bn>7: 
                mapbnmrecal[y_index+offw][x_index]=4
            
            
    for x_index in range(20):
        for y_index in range(13):
            bnre=mapbnmrecal[y_index+offw][x_index]
            bn=mapbnm[y_index+offw][x_index]
            if bn==0: surface1.blit(bild0,[x_index*16,y_index*16-offr])
            if bn==1: surface1.blit(bild1,[x_index*16,y_index*16-offr])
            if bn==2: surface1.blit(bild2,[x_index*16,y_index*16-offr])
            if bn==3: surface1.blit(bild3,[x_index*16,y_index*16-offr])
            if bn==4: surface1.blit(bild4,[x_index*16,y_index*16-offr])
            if bn==5: surface1.blit(bild5,[x_index*16,y_index*16-offr])
            if bn==6: surface1.blit(bild6,[x_index*16,y_index*16-offr])
            if bn==7: surface1.blit(bild7,[x_index*16,y_index*16-offr])
            if bn==8: surface1.blit(bild8,[x_index*16,y_index*16-offr])
#            pygame.draw.rect(screen,Colourmap[cm_index],[x_index,y_index,1,1])
#    text_bild=stil.render("1",True,[0,0,0])
#    screen.blit(text_bild,[25,25])
    
#    bild=pygame.image.load("check.png").convert()
    surface2 = pygame.transform.scale(surface1, sz)
    screen.blit(surface2,[0,0])
    pygame.display.flip()
    clock.tick(60)
pygame.quit()