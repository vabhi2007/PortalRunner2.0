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

RightCharacter = pygame.image.load("Sprites/Right.png")
LeftCharacter = pygame.image.load("Sprites/Left.png")

DisplayX = 700
DisplayY = 500
Display = pygame.display.set_mode((DisplayX, DisplayY))
Display.fill(white)



class Platform:
    width = 125
    height = 25
    color = black

def MakePlatform (x,y):
    pygame.draw.rect(Display,Platform.color,(x,y,Platform.width, Platform.height))

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
    global centerX,centerY, PossibleMovementCoords
    PossibleMovementCoords.clear()
    MakePlatform(centerX-275, centerY-150)
    PossibleMovementCoords.append((centerX-275, centerY-150))
    MakePlatform(centerX+300,centerY+50)
    PossibleMovementCoords.append((centerX + 300, centerY + 50))

def canMove ():
    global PossibleMovementCoords, CharacterX,CharacterY
    print(PossibleMovementCoords)
    for coord in PossibleMovementCoords:
        print(coord)
        X = coord[0]
        Y = coord[1]
        if CharacterX > X-9 and CharacterX < X + 125 + 9:
            print("Hi")
            return True

def checkKey ():
    global centerX,centerY,CharacterDirection,PossibleMovementCoords
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if canMove() == True:
                if event.key == pygame.K_a:

                    centerX+=10
                    CharacterDirection = 'left'
                elif event.key == pygame.K_d:
                    centerX-=10
                    CharacterDirection = 'right'

font = pygame.font.Font('freesansbold.ttf',32)
while True:
    clock.tick(100)
    seconds+=0.01
    text = font.render(str(math.floor(seconds)), True, black)
    Display.blit(text, (650, 50))

    LoadLevel(1)
    checkKey()
    makeCharacter(CharacterDirection)


    pygame.display.update()
    pygame.draw.rect(Display, white, (0, 0, 700, 500))

# GameObjects = []
# Object = (Display,(0,0,255),(50,50,100,100),2)
# GameObjects.append(Object)
# for Shape in GameObjects:
#     pygame.draw.rect(Shape[0], Shape[1], Shape[2])
#     pygame.display.update()