import pygame
import time
#test
try:
    pygame.init()
except False:
    print("Fail")
else:
    print("Success")
# Basic Colors
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

RightCharacter = pygame.image.load("Sprites/Right.png")
LeftCharacter = pygame.image.load("Sprites/Left.png")

DisplayX = 500
DisplayY = 400
Display = pygame.display.set_mode((DisplayX, DisplayY))
Display.fill(white)

GameObjects = []
Object = (Display,(0,0,255),(50,50,100,100),2)
GameObjects.append()
pygame.draw.rect(Object[0],Object[1],Object[2])
def RefreshEvn():
    for Object in GameObjects:
        pygame.draw.rect(Object)
    pygame.display.update()
while True:
    RefreshEvn()
    pass