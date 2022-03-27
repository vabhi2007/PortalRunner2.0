import math

import pygame
import time

clock = pygame.time.Clock()
seconds = 0
try:
    pygame.init()
except False:
    print("Fail")
else:
    print("Success")
# Basic Colors
black = (0,0,0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

platform = pygame.image.load("Sprites/Platform.png")
background = pygame.image.load("Sprites/Background.png")
bluePortal = pygame.image.load("Sprites/BluePortal.png")
redPortal = pygame.image.load("Sprites/RedPortal.png")
RightCharacter = pygame.image.load("Sprites/Right.png")
LeftCharacter = pygame.image.load("Sprites/Left.png")

DisplayX = 700
DisplayY = 500
Display = pygame.display.set_mode((DisplayX, DisplayY))
Display.fill(white)



class Platform:
    width = 150
    height = 25
    color = black

def MakePlatform (x,y):
    Display.blit(platform,(x,y))

def LoadLevel(level):
    if level == 1:
        Level1()
    pass


CharacterX = 75
CharacterY = 50
CharacterDirection = 'right'
def makeCharacter (direction):
    if direction == 'right':
        Display.blit(RightCharacter, (CharacterX, CharacterY))
    else:
        Display.blit(LeftCharacter, (CharacterX, CharacterY))
PossibleMovementCoords = []

centerX = 350
centerY = 250
def Level1():
    global centerX,centerY, PossibleMovementCoords, seconds
    PossibleMovementCoords.clear()
    MakePlatform(centerX-275, centerY-150)
    PossibleMovementCoords.append((centerX-275, centerY-150))
    if seconds<=5:
        MakePlatform(centerX+300,centerY+50)
        PossibleMovementCoords.append((centerX + 300, centerY + 50))
    seconds+=0.01
def checkKey ():
    global centerX,centerY,CharacterDirection,PossibleMovementCoords, CharacterX, CharacterY
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            for Coord in PossibleMovementCoords:
                CoordX = Coord[0]
                CoordY = Coord[1]
                print(CoordX, CoordY)
                print(CharacterY + 85)
                print(CoordY-85)
                if CharacterY + 85 >= CoordY and CoordY - 45 >= CharacterY:
                    print(Coord)
                    if CharacterX - 10 >= CoordX and CharacterX + 30 <= CoordX + Platform.width:
                        if event.key == pygame.K_a:
                            centerX+=10
                            CharacterDirection = 'left'
                        elif event.key == pygame.K_d:
                            centerX-=10
                            CharacterDirection = 'right'
                        break
                    elif CharacterX - 20 >= CoordX:
                        if event.key == pygame.K_a:
                            centerX+=10
                            CharacterDirection = 'left'
                        break
                    elif CharacterX + 20 <= CoordX + Platform.width:
                        if event.key == pygame.K_d:
                            centerX-=10
                            CharacterDirection = 'right'
                        break

font = pygame.font.Font('freesansbold.ttf',32)
while True:
    clock.tick(100)
    #seconds+=0.01
    text = font.render(str(math.floor(seconds)), True, black)
    Display.blit(text, (650, 50))

    LoadLevel(1)
    makeCharacter(CharacterDirection)
    checkKey()


    pygame.display.update()
    Display.blit(background,(0,0))

# GameObjects = []
# Object = (Display,(0,0,255),(50,50,100,100),2)
# GameObjects.append(Object)
# for Shape in GameObjects:
#     pygame.draw.rect(Shape[0], Shape[1], Shape[2])
#     pygame.display.update()