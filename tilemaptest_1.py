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


# =============================================================================
# create CPC ColourMAP
# =============================================================================
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


# =============================================================================
# init game
# =============================================================================
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
bild10=pygame.image.load("test_10.png").convert()

bild11=pygame.image.load("tilemap2.png").convert()


# =============================================================================
# create surface
# =============================================================================
size = width, height = (320, 200)
surface1 = pygame.Surface(size)

sz = surface1.get_size()
sz = [int(sz[0] * scale), int(sz[1] * scale)]

# =============================================================================
# build 
# =============================================================================
    # Die Tilemap Klasse verwaltet die Tile-Daten, die das Aussehen der Karte beschreiben.

class Tilemap(object):

        def __init__(self):

            # Wir erstellen ein neues Tileset.

            # Hier im Tutorial fügen wir manuell vier Tile-Typen hinzu.

            self.tileset = Tileset.Tileset("tileset.png", (255, 0, 255), 32, 32)

            self.tileset.add_tile("grass", 0, 0)

            self.tileset.add_tile("mud", 32, 0)

            self.tileset.add_tile("water", 64, 0)

            self.tileset.add_tile("block", 0, 32)
            
            # Festlegen der Startposition der Kamera. Hier (0, 0).

            self.camera_x = 0

            self.camera_y = 0

     

            # Die Größe der Maps in Tiles.

            self.width = 30

            self.height = 25

     

            # Erstellen einer leeren Liste für die Tile Daten.

            self.tiles = list()
            map = Tilemap.Tilemap() 
            # Manuelles Befüllen der Tile-Liste:
            # Jedes Feld bekommt ein zufälliges Tile zugewiesen.

            for i in range(0, self.height):

                self.tiles.append(list())

                for j in range(0, self.width):

                    x = random.randint(0, 4)

                    if x == 0:

                        self.tiles[i].append("grass")

                    elif x == 1:

                        self.tiles[i].append("water")

                    elif x == 2:

                        self.tiles[i].append("mud")

                    else:

                        self.tiles[i].append("block")
                # Hier rendern wir den sichtbaren Teil der Karte.

        def render(self, screen):

            # Zeilenweise durch die Tiles durchgehen.

            for y in range(0, int(screen.get_height() / self.tileset.tile_height) + 1):

                # Die Kamera Position mit einbeziehen.

                ty = y + self.camera_y
                if ty >= self.height or ty < 0:

                    continue

                # Die aktuelle Zeile zum einfacheren Zugriff speichern.

                line = self.tiles[ty]

                # Und jetzt spaltenweise die Tiles rendern.

                for x in range(0, int(screen.get_width() / self.tileset.tile_width) + 1):

                    # Auch hier müssen wir die Kamera beachten.
                    map.render(screen)
                    tx = x + self.camera_x
                    if tx >= self.width or tx < 0:

                        continue

                    # Wir versuchen, die Daten des Tiles zu bekommen.

                    tilename = line[tx]
                    tile = self.tileset.get_tile(tilename)

                    # Falls das nicht fehlschlägt können wir das Tile auf die screen-Surface blitten.

                    if tile is not None:

                        screen.blit(self.tileset.image, (x * self.tileset.tile_width, y * self.tileset.tile_height), tile.rect)



            
            
