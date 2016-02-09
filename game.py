# 1 - Import library
import pygame
from pygame.locals import *
 
# 2 - Initialize the game
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
 
# 3 - Load images
cat = pygame.image.load("cat.png")
player = cat.get_rect()

# 4 - keep looping through
while 1:
    # 5 - clear the screen before drawing it again
    screen.fill((255,255,255))
    # 6 - draw the screen elements
    screen.blit(cat, player)
    # 7 - update the screen
    pygame.display.flip()
    # 8 - loop through the events
    for event in pygame.event.get():
        # check if the event is the X button 
        if event.type==pygame.QUIT:
            # if it is quit the game
            exit(0)
        # check if arrow keys are pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player = player.move(0,-5)
            elif event.key == pygame.K_DOWN:
                player = player.move(0,5)
            elif event.key == pygame.K_RIGHT:
                player = player.move(5,0)
            elif event.key == pygame.K_LEFT:
                player = player.move(-5, 0)
               
