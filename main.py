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
black = (0, 0, 0)
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

redPortalCoord = 0
bluePortalCoord = 0

DisplayX = 700
DisplayY = 500
Display = pygame.display.set_mode((DisplayX, DisplayY))
Display.fill(white)
pygame.mouse.set_cursor(pygame.cursors.arrow)
pygame.mouse.set_visible(False)
blueCursor = pygame.image.load("Sprites/Blue Cursor.png")
redCursor = pygame.image.load("Sprites/RedCursor.png")
defaultCursor = pygame.image.load("Sprites/DefaultCursor.png")
variation = 'default'
RedPortal = []
BluePortal = []


class Platform:
    width = 150
    height = 25
    color = black


def MakePlatform(x, y):
    Display.blit(platform, (x, y))


def LoadLevel(level):
    if level == 1:
        Level1()
    pass


CharacterX = 75
CharacterY = 50
CharacterDirection = 'right'


def makeCharacter(direction):
    if direction == 'right':
        Display.blit(RightCharacter, (CharacterX, CharacterY))
    else:
        Display.blit(LeftCharacter, (CharacterX, CharacterY))


PossibleMovementCoords = []

centerX = 350
centerY = 250


def Level1():
    global centerX, centerY, PossibleMovementCoords, seconds
    PossibleMovementCoords.clear()
    MakePlatform(centerX - 275, centerY - 150)
    PossibleMovementCoords.append((centerX - 275, centerY - 150))
    MakePlatform(centerX + 300, centerY + 50)
    PossibleMovementCoords.append((centerX + 300, centerY + 50))
                                   # Example of disappearing platform
    # if seconds<=5:
    #     MakePlatform(centerX+300,centerY+50)
    #     PossibleMovementCoords.append((centerX + 300, centerY + 50))
    seconds += 0.01


def checkKey():
    global centerX, centerY, CharacterDirection, PossibleMovementCoords, CharacterX, CharacterY, variation, RedPortal, BluePortal
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            for Coord in PossibleMovementCoords:
                CoordX = Coord[0]
                CoordY = Coord[1]
                if CharacterY + 85 >= CoordY and CoordY - 45 >= CharacterY:
                    if CharacterX - 10 >= CoordX and CharacterX + 30 <= CoordX + Platform.width:
                        if event.key == pygame.K_a:
                            if len(RedPortal) > 0:
                                RedPortal[0][1][0] += 10
                            if len(BluePortal) > 0:
                                BluePortal[0][1][0] += 10
                            centerX += 10
                            CharacterDirection = 'left'
                        elif event.key == pygame.K_d:
                            if len(RedPortal) > 0:
                                RedPortal[0][1][0] -= 10
                            if len(BluePortal) > 0:
                                BluePortal[0][1][0] -= 10
                            centerX -= 10
                            CharacterDirection = 'right'

                        break
                    elif CharacterX - 20 >= CoordX:
                        if event.key == pygame.K_a:
                            if len(RedPortal) > 0:
                                RedPortal[0][1][0] += 10
                            if len(BluePortal) > 0:
                                BluePortal[0][1][0] += 10
                            centerX += 10
                            CharacterDirection = 'left'
                        break
                    elif CharacterX + 20 <= CoordX + Platform.width:
                        if event.key == pygame.K_d:
                            if len(RedPortal) > 0:
                                RedPortal[0][1][0] -= 10
                            if len(BluePortal) > 0:
                                BluePortal[0][1][0] -= 10
                            centerX -= 10
                            CharacterDirection = 'right'
                        break

            if len(RedPortal) > 0 and len(BluePortal) > 0:
                if CharacterDirection == 'right':
                    if CharacterX + 29 >= RedPortal[0][1][0] and CharacterX + 29 <= RedPortal[0][1][0] + 28:
                        if CharacterY <= RedPortal[0][1][1] + 50 and CharacterY + 50 >= RedPortal[0][1][1]:
                            CharacterX = BluePortal[0][1][0]
                            CharacterY = BluePortal[0][1][1]
                    elif CharacterX + 29 >= BluePortal[0][1][0] and CharacterX + 29 <= BluePortal[0][1][0] + 28:
                        if CharacterY <= BluePortal[0][1][1] + 50 and CharacterY + 50 >= BluePortal[0][1][1]:
                            CharacterX = RedPortal[0][1][0]
                            CharacterY = RedPortal[0][1][1]
                elif CharacterDirection == 'left':
                    if CharacterX >= RedPortal[0][1][0] and CharacterX<= RedPortal[0][1][0] + 28:
                        if CharacterY <= RedPortal[0][1][1] + 50 and CharacterY + 50 >= RedPortal[0][1][1]:
                            print("hi")
                            print(BluePortal[0][1][0])
                            print(RedPortal[0][1][0])
                            CharacterX = BluePortal[0][1][0]
                            CharacterY = BluePortal[0][1][1]
                    elif CharacterX>= BluePortal[0][1][0] and CharacterX<= BluePortal[0][1][0] + 28:
                        if CharacterY <= BluePortal[0][1][1] + 50 and CharacterY + 50 >= BluePortal[0][1][1]:
                            CharacterX = RedPortal[0][1][0]
                            CharacterY = RedPortal[0][1][1]

            if event.key == pygame.K_2:
                variation = 'red'
            if event.key == pygame.K_3:
                variation = 'blue'
            if event.key == pygame.K_1:
                variation = 'default'
        elif event.type == pygame.MOUSEBUTTONDOWN:
            addPortal()


def addPortal():
    global variation, RedPortal, BluePortal
    if variation == 'red':
        RedPortal.clear()
        RedPortal.append((redPortal, list(pygame.mouse.get_pos())))
    elif variation == 'blue':
        BluePortal.clear()
        BluePortal.append((bluePortal, list(pygame.mouse.get_pos())))


def makePortal():
    global RedPortal, BluePortal
    for item in RedPortal:
        Display.blit(item[0], item[1])
    for item in BluePortal:
        Display.blit(item[0], item[1])


def makeCursor():
    global variation
    if variation == 'red':
        Display.blit(redCursor, pygame.mouse.get_pos())
    elif variation == 'blue':
        Display.blit(blueCursor, pygame.mouse.get_pos())
    else:
        Display.blit(defaultCursor, pygame.mouse.get_pos())


font = pygame.font.Font('freesansbold.ttf', 32)
while True:
    clock.tick(100)
    # seconds+=0.01
    text = font.render(str(math.floor(seconds)), True, black)
    Display.blit(text, (650, 50))

    makeCursor()

    LoadLevel(1)
    makeCharacter(CharacterDirection)
    makePortal()
    checkKey()

    pygame.display.update()
    Display.blit(background, (0, 0))

# GameObjects = []
# Object = (Display,(0,0,255),(50,50,100,100),2)
# GameObjects.append(Object)
# for Shape in GameObjects:
#     pygame.draw.rect(Shape[0], Shape[1], Shape[2])
#     pygame.display.update()
