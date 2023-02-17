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


#carImg = pygame.image.load('hexagonCurve.png')

#carImg = pygame.transform.scale(carImg, (90,90))


#def car(x,y):
#    screen.blit(carImg, (x,y))

#x =  (width * 0.10)
#y = (height * 0.10)


#car(x,y)

#carImg.image.fill(transparent)

#Opens window
pygame.display.update()




#Keeps screen running and open
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

game = GameRunner(3)
