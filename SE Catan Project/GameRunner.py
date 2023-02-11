import pygame

#Board view set up
background_colour = (0,131,185)
(width, height) = (1024, 768)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('The Settlers')
screen.fill(background_colour)



carImg = pygame.image.load('hexagon.png')

def car(x,y):
    screen.blit(carImg, (x,y))

x =  (width * 0.45)
y = (height * 0.8)

#Opens window
pygame.display.flip()

car(x,y)


#Keeps screen running and open
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
