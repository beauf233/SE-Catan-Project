import pygame

#Board view set up
background_colour = (0,131,185)
(width, height) = (1024, 768)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Catan Game')
screen.fill(background_colour)

#Opens window
pygame.display.flip()

#Keeps screen running and open
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
