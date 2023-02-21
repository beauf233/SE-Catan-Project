import pygame
from cardTypes import DevCard
import random
from runGame import GameRunner

#Board view set up
background_colour = (0,131,185)
(width, height) = (1024, 768)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('The Settlers')
screen.fill(background_colour)

#transparent = (0, 0, 0, 0)

carImg = pygame.image.load('hexagonCurve.png')

carImg = pygame.transform.scale(carImg, (90,90))

def car(x,y):
    screen.blit(carImg, (x,y))

x =  (width * 0.10)
y = (height * 0.10)


car(x,y)

#carImg.image.fill(transparent)

#Opens window
#pygame.display.update()

def shuffleHexagonTiles():
    hexagonTiles = []

    #Number of each hexagon tiles in the game
    desert = 1
    mountains = 3
    hills = 3
    fields = 4
    pasture = 4
    forest = 4

    #how many different types of hexagons there are
    hexagonNumbers = [0,1,2,3,4,5]

    while deserts + mmountains + hills + fields + pasture + forest == 19
        hexPlacement = random.choice(hexagonNumbers)

        match pick:
            case 0:
                hexagonTiles.append(HexTiles.Desert)
                Desert -= 1
                if Desert == 0:
                    del hexagonTiles[hexagonTiles.index(0)]
            case 1:
                hexagonTiles.append(HexTiles.Mountains)
                Mountains -= 1
                if Mountains == 0
                    del hexagonTiles[hexagonTiles.index(1)]
            case 2:
                hexagonTiles.append(HexTiles.Hills)
                Hills -= 1
                if Hills == 0
                    del hexagonTiles[hexagonTiles.index(2)]
            case 3:
                hexagonTiles.append(HexTiles.Fields)
                Fields -= 1
                if Fields == 0
                    del hexagonTiles[hexagonTiles.index(3)]
            case 4:
                hexagonTiles.append(HexTiles.Pasture)
                Pasture -= 1
                if Pasture == 0
                    del hexagonTiles[hexagonTiles.index(4)]
            case 5:
                hexagonTiles.append(HexTiles.Forest)
                Forest -= 1
                if Forest == 0
                    del hexagonTiles[hexagonTiles.index(5)]
        return hexagonNumbers


#Keeps screen running and open
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

game = GameRunner(3)

